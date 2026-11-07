import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_paragraph(self):
        block = "This is a normal paragraph."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading(self):
        block = "# My Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)


    def test_heading_too_many_hashes(self):
        block = "############### My Heading"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.HEADING)


    def test_heading_no_space(self):
        block = "###############My Heading"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_code_block(self):
        block = "```\nprint('hello world')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_code_block_missing_closing(self):
        block = "```\nprint('hello world')"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote\n> Another line of the quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_block_invalid_line(self):
        block = "> This is a quote\nThis line breaks the quote"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item one\n- item two\n- item three"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_missing_space(self):
        block = "- item one\n-item two"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. first item\n2. second item\n3. third item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_skipped_number(self):
        block = "1. first item\n3. third item"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.ORDERED_LIST)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_quote_with_blank_line(self):
        markdown = '> "I am in fact a Hobbit in all but size."\n>\n> -- J.R.R. Tolkien'
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        print(html)


    def test_code_block_rendering(self):
        markdown = "```\nfunc main(){\n    fmt.Println(\"Aiya, Ambar!\")\n}\n```"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        print(html)


    def test_unordered_list_with_links(self):
        markdown = "- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)\n- [Why Tom Bombadil Was a Mistake](/blog/tom)"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        print(html)


    def test_standalone_image(self):
        markdown = "![JRR Tolkien sitting](/images/tolkien.png)"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        print(html)
        
    def test_ordered_list_long(self):
        markdown = "1. Gandalf\n2. Bilbo\n3. Sam\n4. Glorfindel\n5. Galadriel\n6. Elrond\n7. Thorin\n8. Sauron\n9. Aragorn"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        print(html)
        
    def test_link_followed_by_period(self):
        markdown = "Want to get in touch? [Contact me here](/contact)."
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        print(html)

if __name__ == "__main__":
    unittest.main()