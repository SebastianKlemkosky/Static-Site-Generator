import unittest
from inline_markdown import split_nodes_delimiter, split_nodes_link, split_nodes_image, text_to_textnodes
from textnode import TextNode, TextType
from markdown_blocks import markdown_to_html_node

class TestInlineMarkdown(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("**bold** at the start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("bold", TextType.CODE), TextNode(" at the start", TextType.TEXT)])

    def test_unclosed_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )
        
    def test_split_image_at_start_and_end(self):
        node = TextNode(
            "![first](https://i.imgur.com/a.png)middle text![second](https://i.imgur.com/b.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "https://i.imgur.com/a.png"),
                TextNode("middle text", TextType.TEXT),
                TextNode("second", TextType.IMAGE, "https://i.imgur.com/b.png"),
            ],
            new_nodes,
        )
        
    def test_split_link_no_links(self):
        node = TextNode("Just plain text with no links here.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
        
    def test_split_image_non_text_node(self):
        node = TextNode("![image](https://i.imgur.com/a.png)", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
        
    def test_full_kitchen_sink(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ],
        nodes,
    )
        
    def test_text_to_textnodes_multiple_bold(self):
        text = "This is **bold** and this is **also bold**"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and this is ", TextType.TEXT),
                TextNode("also bold", TextType.BOLD),
            ],
            nodes,
        )     

    def test_text_to_textnodes_link_and_image(self):
        text = "This is a [link](https://boot.dev) and an ![image](https://boot.dev/img.png)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://boot.dev/img.png"),
            ],
            nodes,
        )
        
    def test_quote_with_blank_line(self):
        markdown = '> "I am in fact a Hobbit in all but size."\n>\n> -- J.R.R. Tolkien'
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        print(html)
     
      
if __name__ == "__main__":
    unittest.main()