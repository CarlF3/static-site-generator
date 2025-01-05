import unittest
from markdownconverter import markdown_to_html_node

class TestMarkdownConverter(unittest.TestCase):

    def test_convert_markdown(self):
        md = """# This is a full md test

## Test cases

This markdown will cover a lot of test cases such as:

- *italic* and **bold** inline text.
- Some `code blocks in the middle` of some text.
- Perhaps a [link](https://www.google.com/) or an image ![cat](cat.png).
- and of course lists

## Ordered list

The following should be a ordered list of animals by average size

1. Blue whale
2. Lion
3. Cat

```
text1 = "hello"
text2 = "world!"
print(f"{text1} {text2}")
```

###### A small heading before a quote

> The problem with information that you read on the Internet is that it is not always true.
> Abraham Linconl
> June 2, 1863



"""
        result = markdown_to_html_node(md)
        expected = """<div><h1>This is a full md test</h1><h2>Test cases</h2><p>This markdown will cover a lot of test cases such as:</p><ul><li><i>italic</i> and <b>bold</b> inline text.</li><li>Some <code>code blocks in the middle</code> of some text.</li><li>Perhaps a <a href="https://www.google.com/">link</a> or an image <img src="cat.png" alt="cat"></img>.</li><li>and of course lists</li></ul><h2>Ordered list</h2><p>The following should be a ordered list of animals by average size</p><ol><li>Blue whale</li><li>Lion</li><li>Cat</li></ol><pre><code>
text1 = "hello"
text2 = "world!"
print(f"{text1} {text2}")
</code></pre><h6>A small heading before a quote</h6><blockquote>The problem with information that you read on the Internet is that it is not always true.
Abraham Linconl
June 2, 1863</blockquote></div>"""
        self.assertEqual(result.to_html(), expected)

if __name__ == "__main__":
    unittest.main()