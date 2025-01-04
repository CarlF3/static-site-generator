from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not node.text_type == TextType.NORMAL:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text)%2 == 0:
            raise Exception("Invalid markdown input")
        for i, text in enumerate(split_text):
            if text == "":
                continue
            if i%2 == 0:
                new_nodes.append(TextNode(text, node.text_type))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        remaining = node.text
        for alt, url in matches:
            sections = remaining.split(f"![{alt}]({url})", 1)
            new_nodes.extend([TextNode(sections[0], TextType.NORMAL), TextNode(alt, TextType.IMAGE, url)])
            remaining = sections[1]
        if not remaining == "":
            new_nodes.append(TextNode(remaining, TextType.NORMAL))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        remaining = node.text
        for link_text, url in matches:
            sections = remaining.split(f"[{link_text}]({url})", 1)
            new_nodes.extend([TextNode(sections[0], TextType.NORMAL), TextNode(link_text, TextType.LINK, url)])
            remaining = sections[1]
        if not remaining == "":
            new_nodes.append(TextNode(remaining, TextType.NORMAL))
    return new_nodes