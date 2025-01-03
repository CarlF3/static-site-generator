from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.children is None or self.children == []:
            raise ValueError("Missing child nodes")
        child_node_strings = []
        for node in self.children:
            child_node_strings.append(node.to_html())
        return f'<{self.tag}{self.props_to_html()}>{"".join(child_node_strings)}</{self.tag}>'