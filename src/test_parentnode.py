import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    print("parentnode test")
    def test_parentnode_none(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [])
            ParentNode("p", None)

    def test_empty_string_tag(self):
        with self.assertRaises(ValueError):
            ParentNode("", [])

    def test_parentnode(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"), LeafNode(None, "Normal text"), ], )
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_output)

    def test_parentnode_nested(self):
        parent = ParentNode("div", [LeafNode("span", "hello"), ParentNode("p", [LeafNode("b", "world")])])
        expexted_output = "<div><span>hello</span><p><b>world</b></p></div>"
        self.assertEqual(parent.to_html(), expexted_output)

    def test_deep_nesting(self):
        node = ParentNode("div", [
            ParentNode("section", [
                ParentNode("article", [
                    LeafNode("p", "text")
                ])
            ])
        ])
        expected_output = "<div><section><article><p>text</p></article></section></div>"
        self.assertEqual(node.to_html(), expected_output)

    def test_parentnode_with_props(self):
        node = ParentNode("div", [], {"class": "container"})
        expected_output = '<div class="container"></div>'
        self.assertEqual(node.to_html(), expected_output)

    def test_empty_child(self):
        node = ParentNode("div", [])
        expected_output = "<div></div>"
        self.assertEqual(node.to_html(), expected_output)