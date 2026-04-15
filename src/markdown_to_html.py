from block_markdown import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    list_htmlnodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        list_htmlnodes.append(block_to_htmlnode(block, block_type))
    all_parent = ParentNode("div", list_htmlnodes)
    return all_parent


def block_to_htmlnode(block, block_type):
    text = block
    if block_type == BlockType.PARAGRAPH:
        text = text.split("\n")
        if len(text) > 1:
            for line in text:
                line = line.strip()
        text = " ".join(text)
        children = text_to_children(text)
        node = ParentNode("p", children)
        return node
    if block_type == BlockType.HEADING:
        heading = block[:6].count("#")
        for i in range(heading - 1):
            text = text.lstrip("#")
        text = text.lstrip("# ")
        children = text_to_children(text)
        node = ParentNode(f"h{heading}", children)
        return node
    if block_type == BlockType.CODE:
        leaf = text_node_to_html_node(TextNode(block.lstrip("```\n").rstrip("```"), TextType.CODE))
        node = ParentNode("pre", [leaf])
        return node
    if block_type == BlockType.QUOTE:
        lines = text.split("\n")
        for i in range(len(lines)):
            lines[i] = lines[i].strip(">").strip()
        text = "\n".join(lines)
        children = text_to_children(text)
        node = ParentNode("blockquote", children)
        return node
    if block_type == BlockType.ULIST:
        lines = text.split("\n")
        list_parents = []
        for line in lines:
            line = line.lstrip("- ")
            list_parents.append(ParentNode("li", text_to_children(line)))
        node = ParentNode("ul", list_parents)
        return node
    if block_type == BlockType.OLIST:
        lines = text.split("\n")
        list_parents = []
        for i in range(len(lines)):
            lines[i] = lines[i].lstrip(f"{i + 1}. ")
            list_parents.append(ParentNode("li", text_to_children(lines[i])))
        node = ParentNode("ol", list_parents)
        return node
        

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes