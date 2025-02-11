import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    print("textnode test")
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("test text 1", TextType.TEXT)
        node2 = TextNode("test text 2", TextType.TEXT)
        node3 = TextNode("test text 1", TextType.BOLD)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        
    def test_is_none(self):
        node = TextNode("test text 1", TextType.TEXT)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()