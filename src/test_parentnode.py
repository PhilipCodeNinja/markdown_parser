import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
                )
        html1 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("p", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ]),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
                )
        html2 = "<p><b>Bold text</b><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>"
        self.assertEqual(node1.to_html(), html1)
        self.assertEqual(node2.to_html(), html2)

    def test_no_children(self):
        with self.assertRaises(ValueError) as _:
            ParentNode("p", None).to_html()

    def test_no_tag(self):
        with self.assertRaises(ValueError) as _:
            ParentNode(None, [LeafNode("b", "Bold text")]).to_html()


if __name__ == "__main__":
    unittest.main()