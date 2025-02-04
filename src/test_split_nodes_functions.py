import unittest


from functions import *

class SplitNodes(unittest.TestCase):
    def test_eq(self):

        testnode_1 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.TEXT)
        testnode_1_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ]
        
        testnode_2 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.TEXT)
        testnode_2_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
            ]
        
        testnode_3 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [hallo] no",
                        TextType.TEXT)
        testnode_3_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode(" and [hallo] no", TextType.TEXT),
            ]
        
        testnode_4 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) and ![hallo] no",
                        TextType.TEXT)
        testnode_4_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
            TextNode(" and ![hallo] no", TextType.TEXT),
            ]
        
        self.assertEqual(split_nodes_link([testnode_1]), testnode_1_result)
        self.assertEqual(split_nodes_image([testnode_2]), testnode_2_result)
        self.assertEqual(split_nodes_link([testnode_3]), testnode_3_result)
        self.assertEqual(split_nodes_image([testnode_4]), testnode_4_result)


if __name__ == "__main__":
    unittest.main()