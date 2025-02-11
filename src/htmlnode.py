
class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_props = ""
        if self.props == None:
            return html_props
        for prop in self.props:
            html_props += f' {prop}="{self.props[prop]}"'
        return html_props
    
    def __repr__(self):
        return f"Tag: {self.tag}\nText: {self.value}\nChild: {self.children}\nProps: {self.props}"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
            )