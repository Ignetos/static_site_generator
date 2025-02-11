import unittest
from functions import split_nodes_delimiter, TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    print("delimiter split test")
    def test_split_nodes_delimiter_with_bold(self):
        nodes = [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_with_italic(self):
        nodes = [TextNode("This is text with a *italic phrase* in the middle", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" in the middle", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_with_code(self):
        nodes = [TextNode("This is text with a `code phrase` in the middle", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code phrase", TextType.CODE),
            TextNode(" in the middle", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_with_no_delimiter(self):
        nodes = [TextNode("This is text with no delimiter", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is text with no delimiter", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_with_unmatched_delimiter(self):
        nodes = [TextNode("This is text with an unmatched **bold phrase", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_split_nodes_delimiter_with_non_text_node(self):
        nodes = [TextNode("This is a link", TextType.LINK, "https://example.com")]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is a link", TextType.LINK, "https://example.com")
        ]
        self.assertEqual(result, expected)
