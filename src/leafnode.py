from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("missing value argument")
        super().__init__(tag, value, None, props)
        self.children = None

    def to_html(self):
        if self.tag == None:
            return self.value
        if self.value == None:
            raise ValueError("value is empty")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        