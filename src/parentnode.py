from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag == None:
            raise ValueError ("ERROR! parentnode has no tag")
        if self.children == None:
            raise ValueError ("ERROR! parentnode has no children")
        children = "".join([child.to_html() for child in self.children])

        return f"<{self.tag}>{children}</{self.tag}>"


    def __repr__(self):
        return f"ParentNode({self.tag}), children: {self.children}, {self.props}"