import unittest


from functions import *

class SplitNodes(unittest.TestCase):
    def test_eq(self):
        # sth1a
        testnode_1 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.TEXT)
        # sth1b
        testnode_1_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ]
        # eq1
        self.assertEqual(split_nodes_link([testnode_1]), testnode_1_result)
        # sth2a
        testnode_2 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.TEXT)
        # sth2b
        testnode_2_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
            ]
        # eq2
        self.assertEqual(split_nodes_image([testnode_2]), testnode_2_result)
        # sth3a
        # sth3b
        # eq3
         
        # sth4a
        # sth4b
        # eq4

        # sth5a
        # sth5b
        # eq5
        pass