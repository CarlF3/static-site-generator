import unittest
from textsplitter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_TextNodes
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

    def test_extract_images(self):
        nodes = [TextNode("This is text with multiple ![multiple_icon](multiple.gif) images ![images_icon](images.png)", TextType.NORMAL)]
        result = split_nodes_image(nodes)
        expected = [TextNode("This is text with multiple ", TextType.NORMAL), TextNode("multiple_icon", TextType.IMAGE, "multiple.gif"), TextNode(" images ", TextType.NORMAL), TextNode("images_icon", TextType.IMAGE, "images.png")]
        self.assertEqual(result, expected)

    def test_extract_links(self):
        nodes = [TextNode("This text has multiple [links](https://www.google.com/) to different [places](https://www.bing.com/).", TextType.NORMAL)]
        result = split_nodes_link(nodes)
        expected = [TextNode("This text has multiple ", TextType.NORMAL), TextNode("links", TextType.LINK, "https://www.google.com/"), TextNode(" to different ", TextType.NORMAL), TextNode("places", TextType.LINK, "https://www.bing.com/"), TextNode(".", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_extract_from_text(self):
        self.maxDiff = None
        text = "This is text with **bold** and *italic* words, a `code block`, a ![cat](cat.png) and a [link](https://boot.dev)"
        result = text_to_TextNodes(text)
        expected = [
            TextNode("This is text with ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" words, a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(", a ", TextType.NORMAL),
            TextNode("cat", TextType.IMAGE, "cat.png"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()