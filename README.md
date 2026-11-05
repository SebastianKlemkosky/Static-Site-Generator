# Static Site Generator

A Python-based static site generator that parses Markdown into an intermediate node tree and converts it to HTML.

## Features So Far

- **HTML Node Representation**:
  - `HTMLNode`: Base class for DOM-like elements with tags, values, children, and attributes.
  - `LeafNode`: Represents HTML elements without children (e.g., `<p>`, `<a>`, `<img>`).
  - `ParentNode`: Represents HTML elements that contain nested children.
- **Text Node Model**:
  - `TextNode`: Represents inline segments of formatted text with types defined by `TextType` (plain text, bold, italic, code, link, image).
  - Conversion utility to transform `TextNode` objects into `LeafNode` HTML objects.
- **Inline Markdown Parser**:
  - Delimiter splitting for bold (`**`), italic (`_`), and inline code (`` ` ``).
  - Regex extraction and node splitting for Markdown images (`![alt](url)`) and links (`[anchor](url)`).
  - `text_to_textnodes`: A unified pipeline function that converts raw text into a structured list of `TextNode` instances.

## Project Structure

```text
.
├── src/
│   ├── htmlnode.py             # HTMLNode, LeafNode, and ParentNode classes
│   ├── textnode.py             # TextNode model and conversion helpers
│   ├── inline_markdown.py      # Markdown splitting and extraction logic
│   ├── test_htmlnode.py        # Unit tests for HTML nodes
│   ├── test_textnode.py        # Unit tests for TextNode classes
│   └── test_inline_markdown.py # Unit tests for inline markdown parsing
├── main.sh                     # Runs the main application entry point
└── test.sh                     # Runs the unit test suite
