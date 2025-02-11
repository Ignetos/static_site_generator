import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    print("leafnode test")
    def test_leafnode(self):
        node = LeafNode("p", "this is a test for leaf node")
        expected_result = "<p>this is a test for leaf node</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_leafnode_none(self):
        with self.assertRaises(ValueError):  # Expect an exception when initializing the node
            LeafNode(None, None)

    def test_leafnode_props(self):
        props = {"href": "https://www.google.com",}
        node = LeafNode("a", "this is a link", props)
        expected_output = '<a href="https://www.google.com">this is a link</a>'
        self.assertEqual(node.to_html(), expected_output)

    def test_leafnode_no_tag(self):
        node = LeafNode(None, "This text has no wrapping tag")
        expected_output = "This text has no wrapping tag"
        self.assertEqual(node.to_html(), expected_output)

    def test_leafnode_empty_props(self):
        node = LeafNode("span", "hello world", {})
        expected_output = "<span>hello world</span>"
        self.assertEqual(node.to_html(), expected_output)

    def test_leafnode_multiple_props(self):
        props = {"src": "image.jpg", "alt": "a picture"}
        node = LeafNode("img", "", props)
        expected_output = '<img src="image.jpg" alt="a picture"></img>'
        self.assertEqual(node.to_html(), expected_output)
