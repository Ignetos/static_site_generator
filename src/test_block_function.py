import unittest
from block_function import block_to_block_type, is_heading, is_code, is_quote, is_unordered_list, is_ordered_list

class TestBlockFunction(unittest.TestCase):
    print("block_function test")

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), "heading")
        self.assertEqual(block_to_block_type("```code```"), "code")
        self.assertEqual(block_to_block_type("> Quote"), "quote")
        self.assertEqual(block_to_block_type("* Unordered list"), "unordered_list")
        self.assertEqual(block_to_block_type("1. Ordered list"), "ordered_list")
        self.assertEqual(block_to_block_type("Just a paragraph"), "paragraph")

    def test_is_heading(self):
        self.assertTrue(is_heading("# Heading"))
        self.assertTrue(is_heading("###### Heading"))
        self.assertFalse(is_heading("####### Not a heading"))
        self.assertFalse(is_heading("No heading"))
        self.assertFalse(is_heading(" # Not a heading"))
        self.assertFalse(is_heading("#Heading"))

    def test_is_code(self):
        self.assertTrue(is_code("```code```"))
        self.assertTrue(is_code("```\ncode\n```"))
        self.assertFalse(is_code("``code``"))
        self.assertFalse(is_code("No code"))
        self.assertFalse(is_code("```code"))
        self.assertFalse(is_code("code```"))

    def test_is_quote(self):
        self.assertTrue(is_quote("> Quote"))
        self.assertTrue(is_quote("> Quote\n> Another line"))
        self.assertFalse(is_quote("Not a quote"))
        self.assertFalse(is_quote("> Quote\nNot a quote"))
        self.assertFalse(is_quote(" > Not a quote"))

    def test_is_unordered_list(self):
        self.assertTrue(is_unordered_list("* Item"))
        self.assertTrue(is_unordered_list("- Item"))
        self.assertTrue(is_unordered_list("* Item\n* Another item"))
        self.assertFalse(is_unordered_list("Not a list"))
        self.assertFalse(is_unordered_list("*Item"))

    def test_is_ordered_list(self):
        self.assertTrue(is_ordered_list("1. Item"))
        self.assertTrue(is_ordered_list("1. Item\n2. Another item"))
        self.assertFalse(is_ordered_list("Not a list"))
        self.assertFalse(is_ordered_list("1. Item\n3. Another item"))
        self.assertFalse(is_ordered_list("1.Item"))
        self.assertFalse(is_ordered_list("1. Item\n2. Another item\n4. Yet another item"))

if __name__ == '__main__':
    unittest.main()