from textnode import TextNode, TextType

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