import unittest
from functions import split_nodes_images, split_nodes_links
from textnode import TextNode, TextType

class TestFunctions(unittest.TestCase):
    print("split functions test")
    def test_split_nodes_images(self):
        old_nodes = [
            TextNode("This is a text with an image ![alt text](http://example.com/image.jpg) in it.", TextType.TEXT),
            TextNode("Another text without image.", TextType.TEXT)
        ]
        result_nodes = split_nodes_images(old_nodes)
        
        expected_nodes = [
            TextNode("This is a text with an image ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "http://example.com/image.jpg"),
            TextNode(" in it.", TextType.TEXT),
            TextNode("Another text without image.", TextType.TEXT)
        ]
        
        self.assertEqual(len(result_nodes), len(expected_nodes))
        for result_node, expected_node in zip(result_nodes, expected_nodes):
            self.assertEqual(result_node.text, expected_node.text)
            self.assertEqual(result_node.text_type, expected_node.text_type)
            self.assertEqual(result_node.url, expected_node.url)

    def test_split_nodes_links(self):
        old_nodes = [
            TextNode("This is a text with a link [link text](http://example.com) in it.", TextType.TEXT),
            TextNode("Another text without link.", TextType.TEXT)
        ]
        result_nodes = split_nodes_links(old_nodes)
        
        expected_nodes = [
            TextNode("This is a text with a link ", TextType.TEXT),
            TextNode("link text", TextType.LINK, "http://example.com"),
            TextNode(" in it.", TextType.TEXT),
            TextNode("Another text without link.", TextType.TEXT)
        ]
        
        self.assertEqual(len(result_nodes), len(expected_nodes))
        for result_node, expected_node in zip(result_nodes, expected_nodes):
            self.assertEqual(result_node.text, expected_node.text)
            self.assertEqual(result_node.text_type, expected_node.text_type)
            self.assertEqual(result_node.url, expected_node.url)

    def test_split_nodes_images_no_image(self):
        old_nodes = [
            TextNode("This is a text without any image.", TextType.TEXT)
        ]
        result_nodes = split_nodes_images(old_nodes)
        
        expected_nodes = [
            TextNode("This is a text without any image.", TextType.TEXT)
        ]
        
        self.assertEqual(result_nodes, expected_nodes)

    def test_split_nodes_links_no_link(self):
        old_nodes = [
            TextNode("This is a text without any link.", TextType.TEXT)
        ]
        result_nodes = split_nodes_links(old_nodes)
        
        expected_nodes = [
            TextNode("This is a text without any link.", TextType.TEXT)
        ]
        
        self.assertEqual(result_nodes, expected_nodes)

