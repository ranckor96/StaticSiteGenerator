import re

from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Invalid Markdown syntax, formatted section not closed")
        delimited = []
        sections = node.text.split(delimiter)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                delimited.append(TextNode(sections[i], TextType.TEXT))
            else:
                delimited.append(TextNode(sections[i], text_type))
        new_nodes.extend(delimited)
    return new_nodes

        
def extract_markdown_images(text):
    alt_text_url = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_text_url


def extract_markdown_links(text):
    anchor_text_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return anchor_text_url


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        for image in images:
            splitter = f"![{image[0]}]({image[1]})"
            node_split = node_text.split(splitter)
            if len(node_split) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if node_split[0] != "":
                new_nodes.append(TextNode(node_split[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = node_split[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        for link in links:
            splitter = f"[{link[0]}]({link[1]})"
            node_split = node_text.split(splitter)
            if len(node_split) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if node_split[0] != "":
                new_nodes.append(TextNode(node_split[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = node_split[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes
