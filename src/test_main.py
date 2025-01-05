import unittest
from main import extract_title

class TestMain(unittest.TestCase):

    def test_extract_title(self):
        md = "# Title"
        result = extract_title(md)
        expected = "Title"
        self.assertEqual(result, expected)

    def test_extract_no_title(self):
        md = "## Title"
        with self.assertRaises(ValueError):
            result = extract_title(md)


if __name__ == "__main__":
    unittest.main()