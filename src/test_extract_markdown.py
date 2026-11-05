import unittest
from extract_markdown import extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_extract_markdown_links(self):
        text ="This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])

    def test_extract_markdown_no_matches(self):
        text = "Just plain text with no markdown formatting whatsoever."
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

    def test_extract_markdown_mixed(self):
        text = "Here is a [link](https://boot.dev) and here is an ![image](https://boot.dev/pic.png)"
        self.assertEqual(
            extract_markdown_links(text),
            [("link", "https://boot.dev")],
        )
        self.assertEqual(
            extract_markdown_images(text),
            [("image", "https://boot.dev/pic.png")],
        )
        
if __name__ == "__main__":
    unittest.main()