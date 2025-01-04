import unittest
from textsplitter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestTextSplitter(unittest.TestCase):
    def test_bold_text(self):
        text = "This is markdown with **VERY IMPORTANT** text"
        delimiter = "**"
        nodes = split_nodes_delimiter([TextNode(text, TextType.NORMAL)], delimiter, TextType.BOLD)
        expected = [TextNode("This is markdown with ", TextType.NORMAL), TextNode("VERY IMPORTANT", TextType.BOLD), TextNode(" text", TextType.NORMAL)]
        self.assertEqual(nodes, expected)
    
    def test_italic_text(self):
        text = "This is markdown with *fancy* text"
        delimiter = "*"
        nodes = split_nodes_delimiter([TextNode(text, TextType.NORMAL)], delimiter, TextType.ITALIC)
        expected = [TextNode("This is markdown with ", TextType.NORMAL), TextNode("fancy", TextType.ITALIC), TextNode(" text", TextType.NORMAL)]
        self.assertEqual(nodes, expected)
    
    def test_code_text(self):
        text = "This is markdown with `a code block`"
        delimiter = "`"
        nodes = split_nodes_delimiter([TextNode(text, TextType.NORMAL)], delimiter, TextType.CODE)
        expected = [TextNode("This is markdown with ", TextType.NORMAL), TextNode("a code block", TextType.CODE)]
        self.assertEqual(nodes, expected)
    
    def test_multiple_texts(self):
        nodes = [TextNode("A cat image", TextType.IMAGE, "cat.png"), TextNode("A **very** cute cat", TextType.NORMAL), TextNode("More Info", TextType.ITALIC)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [TextNode("A cat image", TextType.IMAGE, "cat.png"), TextNode("A ", TextType.NORMAL), TextNode("very", TextType.BOLD), TextNode(" cute cat", TextType.NORMAL), TextNode("More Info", TextType.ITALIC)]
        self.assertEqual(result, expected)
        pass

    def test_wrong_markdown(self):
        text = "This text has markdown that is *improperly formated"
        delimiter = "*"
        with self.assertRaises(Exception):
            nodes = split_nodes_delimiter([TextNode(text, TextType.NORMAL)], delimiter, TextType.ITALIC)

    def test_missing_delimiter(self):
        text = "This is text that does not have the delimiter"
        delimiter = "`"
        nodes = split_nodes_delimiter([TextNode(text, TextType.NORMAL)], delimiter, TextType.CODE)
        expected = [TextNode(text, TextType.NORMAL)]
        self.assertEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()