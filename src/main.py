from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
from extract_markdown import extract_markdown_images, extract_markdown_links


def main():
    node = TextNode(
        "Start ![cat](https://example.com/cat.png) middle ![dog](https://example.com/dog.png) end",
        TextType.TEXT,
    )
    result = split_nodes_image([node])
    for n in result:
        print(n)
if __name__ == "__main__":
    main()