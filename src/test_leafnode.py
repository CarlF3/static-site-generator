import unittest
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_with_tag(self):
        node = LeafNode("p", "This is a paragraph leaf node")
        result = "<p>This is a paragraph leaf node</p>"
        self.assertEqual(node.to_html(), result)

    def test_without_tag(self):
        node = LeafNode(None, "This is plain text")
        self.assertEqual(node.to_html(), "This is plain text")

    def test_with_props(self):
        node = LeafNode("a", "A link to Google", {"href": "https://www.google.com"})
        result = '<a href="https://www.google.com">A link to Google</a>'
        self.assertEqual(node.to_html(), result)

if __name__ == "__main__":
    unittest.main()