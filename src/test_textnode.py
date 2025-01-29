import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This node is different", TextType.BOLD)
        node5 = TextNode("This is a text node", TextType.BOLD, "www.link.internet")
        node6 = TextNode("This is a text node", TextType.BOLD, "www.link.internet")
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node3, node2)
        self.assertNotEqual(node1, node4)
        self.assertNotEqual(node1, node5)
        self.assertEqual(node5, node6)
 

if __name__ == "__main__":
    unittest.main()
