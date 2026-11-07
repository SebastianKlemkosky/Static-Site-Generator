import unittest
import os
import shutil

from gencontent import extract_title, generate_page


class TestGenContent(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = "# Hello"
        title = extract_title(markdown)
        self.assertEqual(title, "Hello")

    def test_extract_title_with_other_content(self):
        markdown = "Some intro text.\n\n# The Real Title\n\nMore content."
        title = extract_title(markdown)
        self.assertEqual(title, "The Real Title")

    def test_extract_title_no_h1(self):
        markdown = "## Not an h1\n\nSome text without a proper title."
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_generate_page_creates_file(self):
        # set up temporary from/template files, call generate_page,
        # then check that dest file was created and contains expected content
        pass


if __name__ == "__main__":
    unittest.main()