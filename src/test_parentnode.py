import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_with_tag(self):
        node = ParentNode("p", [
                LeafNode("b", "Bolded text"),
                LeafNode(None, "Some plain text"),
                LeafNode("a","A link", {"href": "https://www.google.com/", "target": "_blank"}, ),
                LeafNode(None, "Some more plain text")
            ])
        result = '<p><b>Bolded text</b>Some plain text<a href="https://www.google.com/" target="_blank">A link</a>Some more plain text</p>'
        self.assertEqual(node.to_html(), result)

    def test_no_childen(self):
        node = ParentNode("div", [])
        self.assertRaises(ValueError)

    def test_no_tag(self):
        node = ParentNode(None, [LeafNode(None, "Some text")])
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()