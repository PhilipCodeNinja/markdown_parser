from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        current_text = ""
        is_text_type = False
        node_text = node.text
        old_node_type = node.text_type
        new_node_type = text_type
        for index, char in enumerate(node_text):
            # current character is not delimiter, collects all but delimiter
            if   char != delimiter: 
                current_text += char
                # end of text, append
                if index == len(node_text) - 1:
                    new_nodes.append(TextNode(current_text, old_node_type))
            # we found the target text
            elif char == delimiter and not is_text_type:
                is_text_type = True
                new_nodes.append(TextNode(current_text, old_node_type))
                current_text = ""
            # target text is over
            elif char == delimiter and     is_text_type:
                is_text_type = False
                new_nodes.append(TextNode(current_text, new_node_type))
                current_text = ""
    return new_nodes



