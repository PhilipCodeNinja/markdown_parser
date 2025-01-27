from textnode import *

def main():
    bold_node = TextNode("I am bold", TextType.BOLD, "www.link.web") # 2nd parameter??
    italic_node = TextNode("I am from Italy", TextType.ITALIC, "www.link.web") # 2nd parameter??
    bold_node_two = TextNode("I am bold", TextType.BOLD, "www.link.web") # 2nd parameter??


    print(bold_node)


if __name__ == "__main__":
    main()