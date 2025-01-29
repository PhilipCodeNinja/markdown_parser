import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestTextNodeToHTMLFunction(unittest.TestCase):
    def test_eq(self):
        # text
        self.assertEqual(text_node_to_html_node(TextNode("Texty", TextType.TEXT)),
                         LeafNode(None, "Texty"))
        # bold
        self.assertEqual(text_node_to_html_node(TextNode("Boldy", TextType.BOLD)),
                         LeafNode("b", "Boldy"))
        # italic
        self.assertEqual(text_node_to_html_node(TextNode("Italy", TextType.ITALIC)),
                         LeafNode("i", "Italy"))
        # code
        self.assertEqual(text_node_to_html_node(TextNode("Codey", TextType.CODE)),
                         LeafNode("code", "Codey"))
        # link
        self.assertEqual(text_node_to_html_node(TextNode("Linky", TextType.LINK, "www.linky.link")),
                         LeafNode("a", "Linky", {"href": "www.linky.link"}))
        # image
        self.assertEqual(text_node_to_html_node(TextNode("Image", TextType.IMAGE, "www.image.com")),
                         LeafNode("img", "", {"src": "www.image.com", "alt": "Image"}))
    def test_text_type_invalid(self):
        with self.assertRaises(Exception) as _:
            text_node_to_html_node(TextNode("Error text node", TextType.WINGDINGS))



if __name__ == "__main__":
    unittest.main()