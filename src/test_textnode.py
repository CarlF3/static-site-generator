import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = str(TextNode("This is a text node", TextType.NORMAL))
        node2 = str(TextNode("This is a text node", TextType.NORMAL))
        self.assertEqual(node, node2)

    def test_define_url_none(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_define_url(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.IMAGE, "./image_url.png")
        self.assertNotEqual(node, node2)

    def test_different_texttype(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_text_to_html(self):
        node = TextNode("Normal text", TextType.NORMAL)
        result = 'Normal text'
        self.assertEqual(node.to_HTMLNode().to_html(), result)

    def test_bold_to_html(self):
        node = TextNode("Bold text", TextType.BOLD)
        result = '<b>Bold text</b>'
        self.assertEqual(node.to_HTMLNode().to_html(), result)

    def test_italic_to_html(self):
        node = TextNode("Italic text", TextType.ITALIC)
        result = '<i>Italic text</i>'
        self.assertEqual(node.to_HTMLNode().to_html(), result)

    def test_img_to_html(self):
        node = TextNode("An image", TextType.IMAGE, "image.png")
        result = '<img src="image.png" alt="An image"></img>'
        self.assertEqual(node.to_HTMLNode().to_html(), result)

    def test_link_to_html(self):
        node = TextNode("A link", TextType.LINK, "https://www.google.com/")
        result = '<a href="https://www.google.com/">A link</a>'
        self.assertEqual(node.to_HTMLNode().to_html(), result)

    def test_code_to_html(self):
        node = TextNode("Some code", TextType.CODE)
        result = '<code>Some code</code>'
        self.assertEqual(node.to_HTMLNode().to_html(), result)

if __name__ == "__main__":
    unittest.main()