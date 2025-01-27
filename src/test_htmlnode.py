import unittest 

from htmlnode import HTMLNode



props1 = {
    "href": "https://www.google.com",
    "target": "_blank",
}

props2 = {
    "href": "https://www.philipreiber.com",
    "target": "_blank",
}


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(props=props1)
        node2 = HTMLNode(props=props1)
        node3 = HTMLNode(props=props2)
        def node1f():
            return node1.props_to_html
        def node2f():
            return node2.props_to_html
        def node3f():
            return node3.props_to_html
        # function calling mindeffery magic
        self.assertEqual(node1f()(), node2f()())
        self.assertEqual(node2f()(), node1f()())
        self.assertNotEqual(node1f()(), node3f()())
        self.assertNotEqual(node3f()(), node2f()())

if __name__ == "__main__":
    unittest.main()
