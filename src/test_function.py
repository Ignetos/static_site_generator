import unittest

from functions import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    print("function test")
    def test_extract_markdown_images(self):
        text = "This is an image ![alt text](http://example.com/image.jpg)"
        expected = [("alt text", "http://example.com/image.jpg")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

        text = "No image here"
        expected = []
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

        text = "Multiple images ![first](http://example.com/first.jpg) and ![second](http://example.com/second.jpg)"
        expected = [("first", "http://example.com/first.jpg"), ("second", "http://example.com/second.jpg")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        text = "This is a link [example](http://example.com)"
        expected = [("example", "http://example.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

        text = "No link here"
        expected = []
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

        text = "Multiple links [first](http://example.com/first) and [second](http://example.com/second)"
        expected = [("first", "http://example.com/first"), ("second", "http://example.com/second")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)