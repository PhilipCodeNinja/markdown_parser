from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from split_old_nodes import split_nodes_delimiter

def main():
    bold_node = TextNode("I am bold", TextType.BOLD, "www.link.web") # 2nd parameter??
    italic_node = TextNode("I am from Italy", TextType.ITALIC, "www.link.web") # 2nd parameter??
    bold_node_two = TextNode("I am bold", TextType.BOLD, "www.link.web") # 2nd parameter??


    node_to_split = TextNode("Hello! *I am seperate!* What?", TextType.TEXT)
    split_nodes = split_nodes_delimiter([node_to_split], "*", TextType.BOLD)
    print("node_to_split: ", node_to_split)
    print("split_nodes: ", split_nodes)


if __name__ == "__main__":
    main()


