import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    print("htmlnode test")
    def test_type(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "test": "prop",
            }
        html_node = HTMLNode("p", "test text for html node", [], props)
        self.assertEqual(type(html_node.tag), str)
        self.assertEqual(type(html_node.value), str)
        self.assertEqual(type(html_node.children), list)
        self.assertEqual(type(html_node.props), dict)

    def test_raise(self):
        html_node = HTMLNode("p", "test text for html node", [], {})
        self.assertRaises(NotImplementedError, html_node.to_html)

    def test_print(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "test": "prop",
            }
        html_node = HTMLNode("p", "test text for html node", [], props)
        expected_output = f"Tag: p\nText: test text for html node\nChild: []\nProps: {props}"
        self.assertEqual(html_node.__repr__(), expected_output)

    def test_props_to_html_none(self):
        html_node = HTMLNode("p", "test text for html node")
        self.assertEqual(html_node.props_to_html(), "")

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "test": "prop",
            }
        html_node = HTMLNode("p", "test text for html node", None, props)
        expected_output =  ' href="https://www.google.com" target="_blank" test="prop"'
        self.assertEqual(html_node.props_to_html(), expected_output)
