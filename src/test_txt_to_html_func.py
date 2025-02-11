import unittest

from functions import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestTxtToHTML(unittest.TestCase):
    print("text to html test")
    def test_function(self):
        node1 = TextNode("this is a test node", TextType.TEXT)
        node2 = TextNode("this is a test node", TextType.BOLD)
        node3 = TextNode("this is a test node", TextType.ITALIC)
        node4 = TextNode("this is a test node", TextType.CODE)
        node5 = TextNode("this is a test node", TextType.LINK, "https://www.google.com")
        node6 = TextNode("this is a test node", TextType.IMAGE, "https://www.google.com")
        self.assertEqual(text_node_to_html_node(node1).to_html(), "this is a test node")
        self.assertEqual(text_node_to_html_node(node2).to_html(), "<b>this is a test node</b>")
        self.assertEqual(text_node_to_html_node(node3).to_html(), "<i>this is a test node</i>")
        self.assertEqual(text_node_to_html_node(node4).to_html(), "<code>this is a test node</code>")
        self.assertEqual(text_node_to_html_node(node5).to_html(), '<a href="https://www.google.com">this is a test node</a>')
        self.assertEqual(text_node_to_html_node(node6).to_html(),
            '<img src="https://www.google.com" alt="this is a test node"></img>')

        