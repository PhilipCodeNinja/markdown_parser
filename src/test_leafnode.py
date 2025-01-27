import unittest

from leafnode import LeafNode

props1 = {
    "href": "https://www.google.com",
    "target": "_blank",
}

props2 = {
    "href": "https://www.philipreiber.com",
    "target": "_blank",
}


class TestLeafNode(unittest.TestCase):
    
    def test_eq(self):
        leaf1 = LeafNode("p", "This is a paragraph", props1)
        leaf2 = LeafNode("p", "This is a paragraph", props1) # as leaf1
        leaf3 = LeafNode("h1", "This is a headline", props1)
        leaf4 = LeafNode(None, "This is plain text", props1) # no tag
        self.assertEqual(leaf1, leaf2)
        self.assertNotEqual(leaf1, leaf3)
        self.assertNotEqual(leaf1, leaf4)

    def test_error(self):
        leaf5 = LeafNode("p", None, props1) # should raise error
        with self.assertRaises(ValueError) as context:
            leaf5.to_html()


if __name__ == "__main__":
    unittest.main()
