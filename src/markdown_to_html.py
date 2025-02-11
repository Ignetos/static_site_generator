import re

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from block_function import block_to_block_type, extract_text_from_block, extract_code_block
from functions import text_node_to_html_node, text_to_textnodes


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = blocks_to_children(blocks)
    return ParentNode("div", children)

def markdown_to_blocks(markdown):
    pattern = r"\s*\n\s*\n\s*"
    blocks = map(lambda x: x.strip(), re.split(pattern, markdown))
    clean_blocks = list(filter(lambda x: x != "", blocks))
    return clean_blocks

def blocks_to_children(blocks: str):
    list_of_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "paragraph":
                list_of_nodes.append(ParentNode("p", text_to_htmlnodes(block, block_type)))
            case "heading":
                header, text = block.split(' ', 1)
                tag = str(len(header))
                list_of_nodes.append(ParentNode(f"h{tag}", text_to_htmlnodes(block, block_type)))
            case "code":
                text = extract_code_block(block)
                node = LeafNode("code", text)
                list_of_nodes.append(ParentNode("pre", [node]))
            case "quote":
                list_of_nodes.append(ParentNode("blockquote", text_to_htmlnodes(block, block_type)))
            case "ordered_list":
                lines = block.split("\n")
                node =[]
                for line in lines:
                    node.append(ParentNode('li', text_to_htmlnodes(line, block_type)))
                list_of_nodes.append(ParentNode('ol', node))
            case "unordered_list":
                lines = block.split("\n")
                node = []
                for line in lines:
                    # Check if this is actually a list item
                    if not line.strip().startswith(('* ', '- ')):
                        # Not a list item, make it a paragraph
                        nodes = list(map(text_node_to_html_node, text_to_textnodes(line)))
                        list_of_nodes.append(ParentNode('p', nodes))
                        continue
                        
                    # Process actual list items
                    content = re.sub(r'^\s*[\*\-]\s+', '', line)
                    nodes = list(map(text_node_to_html_node, text_to_textnodes(content)))
                    node.append(ParentNode("li", nodes))
                
                if node:  # Only create ul if we have list items
                    list_of_nodes.append(ParentNode('ul', node))
                    
            case _:
                list_of_nodes.append(ParentNode("p", text_to_htmlnodes(block, "paragraph")))

    return list_of_nodes

def text_to_htmlnodes(block, type="paragraph"):
    text_nodes = extract_text_from_block(block, type)
    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
    return html_nodes