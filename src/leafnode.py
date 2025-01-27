from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)


    def to_html(self):
        if not self.tag:
            if not self.value:
                raise ValueError ("All leaves must have value.")
            else:
                return f"{self.value}"
        else:
            if not self.value:
                raise ValueError ("All leaves must have value.")
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        return (self.tag == other.tag) and (self.value == other.value) and (self.props == other.props)


    def __repr__(self):
        return (f"tag: {self.tag}, "
                f"value: {self.value}, "
                f"props: {self.props}")