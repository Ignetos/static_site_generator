import re

from textnode import TextNode, TextType
from leafnode import LeafNode
from constants import DELIMITERS

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError("Invalid type passed for text_node.text_type.")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": f"{text_node.url}",})
        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError(f"A URL is required for Image Type, but got: {text_node.url}")
            text_value = text_node.text if text_node.text is not None else ""
            return LeafNode("img", "", props={"src": f"{text_node.url}", "alt": f"{text_value}"})
        case _:
            raise Exception("unexpected error")
        
def split_nodes_delimiter(old_nodes: list, delimiter, text_type):
    result_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_list.append(node)
            continue

        text = node.text
        first_delimiter = text.find(delimiter)

        if first_delimiter == -1:
            result_list.append(node)
            continue

        second_delimiter = text.find(delimiter, first_delimiter + len(delimiter))
        if second_delimiter == -1:
            raise ValueError(f"No closing delimiter {delimiter} found")
        
        # For the first part (before first delimiter)
        before_text = text[0:first_delimiter]
        if before_text:  # only append if not empty
            result_list.append(TextNode(before_text, TextType.TEXT))

        # For the middle part (between delimiters)
        middle_text = text[first_delimiter + len(delimiter):second_delimiter]
        result_list.append(TextNode(middle_text, text_type))

        # For the last part (after second delimiter)
        after_text = text[second_delimiter + len(delimiter):]
        if after_text:  # only append if not empty
            result_list.append(TextNode(after_text, TextType.TEXT))

    return result_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_images(old_nodes: list):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    text_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_node.append(node)
            continue
        sections = re.split(pattern, node.text)
        for i in range(len(sections)):
            if i % 3 == 0:  # Handle text parts
                if sections[i]:  # Skip creating an empty text node
                    text_node.append(TextNode(sections[i], TextType.TEXT))
            elif i % 3 == 1:  # Handle image `alt text`
                alt_text = sections[i]
                url = sections[i+1]  # The URL is always the next odd-indexed item
                text_node.append(TextNode(alt_text, TextType.IMAGE, url))

    return text_node

def split_nodes_links(old_nodes: list):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    text_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_node.append(node)
            continue
        sections = re.split(pattern, node.text)
        for i in range(len(sections)):
            if i % 3 == 0:  # Handle text parts
                if sections[i]:  # Skip creating an empty text node
                    text_node.append(TextNode(sections[i], TextType.TEXT))
            elif i % 3 == 1:  # Handle image `alt text`
                text = sections[i]
                url = sections[i+1]  # The URL is always the next odd-indexed item
            # Check for validity of the link
                if text and url:
                    text_node.append(TextNode(text, TextType.LINK, url))
                else:
                    # If invalid (empty alt or URL), treat as plain text
                    invalid_link = f"[{text}]({url})"
                    text_node.append(TextNode(invalid_link, TextType.TEXT))

    return text_node

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT),]
    nodes = process_delimiters(nodes)
    nodes = process_links_and_images(nodes)
    return nodes

def process_delimiters(nodes):
    result = nodes
    for delimiter, text_type in DELIMITERS:
        result = split_nodes_delimiter(result, delimiter, text_type)
    return result

def process_links_and_images(nodes):
    result = split_nodes_images(nodes)
    result = split_nodes_links(result)
    return result