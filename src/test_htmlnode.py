import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = str(HTMLNode("p", "Test HTML paragraph node"))
        node2 = "HTMLNode(p, Test HTML paragraph node, None, None)"
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com", "target": "_blank",})
        props_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), props_string)

    def test_different_nodes(self):
        node = str(HTMLNode("p", "Test HTML paragraph node"))
        node2 = str(HTMLNode("a", "Test HTML link/anchor node", None, {"href": "https://www.google.com/", "target": "_blank"}))
        self.assertNotEqual(node, node2)

    def test_leaf_node_tag(self):
        node = LeafNode("p", "This is a paragraph leaf node")
        result = "<p>This is a paragraph leaf node</p>"
        self.assertEqual(node.to_html(), result)

    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "This is plain text")
        self.assertEqual(node.to_html(), "This is plain text")

    def test_leaf_node_props(self):
        node = LeafNode("a", "A link to Google", {"href": "https://www.google.com"})
        result = '<a href="https://www.google.com">A link to Google</a>'
        self.assertEqual(node.to_html(), result)

if __name__ == "__main__":
    unittest.main()