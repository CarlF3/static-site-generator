from markdownblocks import markdown_to_blocks, block_to_block_type, BlockType
from parentnode import ParentNode
from leafnode import LeafNode
from textsplitter import text_to_TextNodes

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block, block_type)
        html_nodes.append(block_node)

    return ParentNode("div", html_nodes)

def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.HEADING:
            return heading_to_html(block)
        case BlockType.CODE:
            return code_to_html(block)
        case BlockType.QUOTE:
            return quote_to_html(block)
        case BlockType.U_LIST:
            return list_to_html(block, False)
        case BlockType.O_LIST:
            return list_to_html(block, True)
        case _:
            return paragraph_to_html(block)
    pass

def text_to_children(text):
    text_nodes = text_to_TextNodes(text)
    child_nodes = []
    for node in text_nodes:
        html_node = node.to_HTMLNode()
        child_nodes.append(html_node)
    return child_nodes

def heading_to_html(heading):
    split = heading.split(" ")
    heading_type = f"h{len(split[0])}"
    children = text_to_children(" ".join(split[1:]))
    return ParentNode(heading_type, children)

def code_to_html(code):
    text = code[3:-3]
    code_node = LeafNode("code", text)
    return ParentNode("pre", [code_node])

def quote_to_html(quote):
    # strip '> ' from each line
    lines = quote.split('\n')
    new_lines = []
    for line in lines:
        new_lines.append(line[2:])
    new_quote = "\n".join(new_lines)
    children = text_to_children(new_quote)
    return ParentNode("blockquote", children)

def list_to_html(md_list, ordered):
    tag = "ol" if ordered else "ul"
    # strip list prefix
    lines = md_list.split('\n')
    new_lines = []
    for line in lines:
        new_line = " ".join(line.split(" ")[1:])
        new_lines.append(new_line)
    # make each list item a list parent node
    children = []
    for line in new_lines:
        node = ParentNode("li", text_to_children(line))
        children.append(node)
    return ParentNode(tag, children)

def paragraph_to_html(paragraph):
    children = text_to_children(paragraph)
    return ParentNode("p", children)