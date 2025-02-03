from enum import Enum

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode


class TextType(Enum):
    TEXT= "text"
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, value: TextType, url=None): # 2nd parameter???
        self.text = text
        self.text_type = value
        self.url = url
    
    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def get_text(self):
        return self.text
    
    def get_text_type(self):
        return self.text_type
    
    def get_url(self):
        return self.url

def text_node_to_html_node(text_node : TextNode):
    text_type = text_node.text_type
    link = text_node.url
    text = text_node.text
    if text_type not in TextType:
        raise Exception ("ERROR! Texttype does not exist")
    if text_type == TextType.TEXT:
        return LeafNode(None, text)
    if text_type == TextType.BOLD:
        return LeafNode("b", text)
    if text_type == TextType.ITALIC:
        return LeafNode("i", text)
    if text_type == TextType.CODE:
        return LeafNode("code", text)
    if text_type == TextType.LINK:
        return LeafNode("a", text, {"href": link}) 
    if text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": link, "alt": text})
