import unittest
from markdownblocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_blocks(self):
        md = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = markdown_to_blocks(md)
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(result, expected)

    def test_markdown_newlines(self):
        md = """# This is a heading





This is a paragraph of text. It has some **bold** and *italic* words inside of it.





* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = markdown_to_blocks(md)
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(result, expected)

    def test_b2bt_heading_1(self):
        md = """# Heading 1"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.HEADING)

    def test_b2bt_heading_4(self):
        md = """#### Heading 4"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.HEADING)

    def test_b2bt_heading_7(self):
        md = """####### Heading 7 doesn't exist"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_b2bt_code(self):
        md = """```
        text1 = "Hello"
        text2 = "World!"
        print(f"{text1} {text2}")
        ```"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.CODE)

    def test_b2bt_open_code(self):
        md = """```
        text1 = "Hello"
        text2 = "World!"
        print(f"{text1} {text2}")
        """
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_b2bt_broken_code(self):
        md = """```
        text1 = "Hello"
        text2 = "World!" ```
        print(f"{text1} {text2}")
        ```"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_b2bt_quote(self):
        md = """> The problem with information that you read on the Internet is that it is not always true.
> Abraham Lincoln, June 2, 1861"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.QUOTE)

    def test_b2bt_broken_quote(self):
        md = """> The problem with information that you read on the Internet is that it is not always true.
Abraham Lincoln, June 2, 1861"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_b2bt_u_list_dash(self):
        md = """- Item
- Another item
- A final item"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.U_LIST)

    def test_b2bt_u_list_asterisk(self):
        md = """* Item
* Another item
* A final item"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.U_LIST)

    def test_b2bt_broken_u_list(self):
        md = """*Item
*Another item
*Final item"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_b2bt_o_list(self):
        md = """1. First item
2. Second item
3. Third item"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.O_LIST)

    def test_b2bt_wrong_start_o_list(self):
        md = """2. Second item
3. Third item
4. Fourth item"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_b2bt_broken_o_list(self):
        md = """2.Second item
3.Third item
4.Fourth item"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_b2bt_paragraph(self):
        md = """This is some basic text
that would go in the markdown
file as a parahraph."""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()