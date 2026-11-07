from enum import Enum
import re
from textnode import text_node_to_html_node, HTMLNode, ParentNode, LeafNode, TextNode, TextType
from inline_markdown import text_to_textnodes

class BlockType (Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block:str) -> BlockType:
    
    if re.match(r"#{1,6} ", block):
        return BlockType.HEADING
    
    if re.match(r"```\n.*```$", block, re.DOTALL):
        return BlockType.CODE
        
    lines = block.split("\n")
    
    result = all(line.startswith(">") for line in lines)
    if result:
        return BlockType.QUOTE
    

    result = all(line.startswith("- ") for line in lines)
    if result:
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True
    for i, line in enumerate(lines, 1):
        expected_prefix = f"{i}. "
        if not line.startswith(expected_prefix):
            is_ordered_list = False
            break

    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = None
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = paragraph_to_html_node(block)

            case BlockType.HEADING:
                html_node = heading_to_html_node(block)

            case BlockType.CODE:
                html_node = code_to_html_node(block)

            case BlockType.QUOTE:
                html_node = quote_to_html_node(block)

            case BlockType.UNORDERED_LIST:
                html_node = unordered_list_to_html_node(block)

            case BlockType.ORDERED_LIST:
                html_node = ordered_list_to_html_node(block)

            case _:
                raise ValueError("unknown block type")
        children.append(html_node)
    return ParentNode("div", children)

def paragraph_to_html_node(block: str) -> HTMLNode:
    block = block.replace("\n", " ")
    children = text_to_children(block)
    return ParentNode("p", children)

def heading_to_html_node(block: str) -> HTMLNode:
    header_level = len(block) - len(block.lstrip("#"))
    block = block[header_level+1:]
    prefix_tag = f"h{header_level}"
    children = text_to_children(block)
    return ParentNode(prefix_tag, children)
    
def code_to_html_node(block: str) -> HTMLNode:
    block = block[4:len(block) - 3]
    raw_text_node = TextNode(block, TextType.CODE)
    node = text_node_to_html_node(raw_text_node)
    
    return ParentNode("pre", [node])

def quote_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip("> "))
        
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)

    
def unordered_list_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    items = []
    for line in lines:
        line = line.lstrip("- ")
        children = text_to_children(line)
        items.append(ParentNode("li", children))
            
    return ParentNode("ul", items)

def ordered_list_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    items = []
    for i, line in enumerate(lines, 1):
        prefix = f"{i}. "
        line = line[len(prefix):]
        children = text_to_children(line)
        items.append(ParentNode("li", children))
            
    return ParentNode("ol", items)



