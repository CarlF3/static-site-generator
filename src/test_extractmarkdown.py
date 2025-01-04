import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_single_image(self):
        text = "This text ends with an image of a cat ![cat](cat.jpg)"
        result = extract_markdown_images(text)
        expected = [("cat", "cat.jpg")]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        text = "This is text with multiple ![multiple_icon](multiple.gif) images ![images_icon](images.png)"
        result = extract_markdown_images(text)
        expected = [("multiple_icon","multiple.gif"), ("images_icon","images.png")]
        self.assertEqual(result, expected)

    def test_single_link(self):
        text = "This text has a single [link](https://www.google.com/)"
        result = extract_markdown_links(text)
        expected = [("link","https://www.google.com/")]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        text = "This text has multiple [links](https://www.google.com/) to different [places](https://www.bing.com/)."
        result = extract_markdown_links(text)
        expected = [("links","https://www.google.com/"), ("places","https://www.bing.com/")]
        self.assertEqual(result, expected)

    def test_without_images(self):
        text = "This text has no links or images."
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_without_links(self):
        text = "This text has no links or images."
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()