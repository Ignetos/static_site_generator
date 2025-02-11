from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        if not tag:
            raise ValueError("missing tag value")
        elif children == None:
            raise ValueError("children list is missing")
        self.value = None

    def to_html(self):
        children_html = ''.join(map(lambda child: child.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
 