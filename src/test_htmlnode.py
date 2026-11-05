import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode



class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            tag="a",
            value="Click here!",
            props={"href": "https://www.boot.dev", "target": "_blank"},
        )

        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_not_eq(self):
        node = HTMLNode(
            tag="a",
            value="Click here!",
            props={"href": "https://www.boot.dev", "target": "_blank"},
        )

        self.assertNotEqual(node.props_to_html(), ' href="https://www.boots.dev" target="_blank"')

    def test_none(self):
        node = HTMLNode(
            tag="a",
            value="Click here!",
            
        )

        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just plain text without a tag.")
        self.assertEqual(node.to_html(), "Just plain text without a tag.")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()