import re
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


def extract_markdown_images(text):
    """
    text: a string containing text and image links in markdown format
    (markdown: ![description](link))
    returns:
        list of tuples, where 
            tuple[X][0] is a string describing the link, and
            tuple[X][1] is a string, a link to the image
    """
    resulting_tuples = []
    image_descriptions_links = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for description_link in image_descriptions_links:
        new_tuple = (description_link[0], description_link[1])
        resulting_tuples.append(new_tuple)
    return resulting_tuples


   # returns [(...), (...)]
   # each (...) contains: alt:..., url:...


def extract_markdown_links(text):
    """
    text: a string containing text and links in markdown format
    (markdown: [description](link))
    returns:
        list of tuples, where 
            tuple[X][0] is a string describing the link, and
            tuple[X][1] is a string, a link
    """
    resulting_tuples = []
    link_descriptions_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for link_description in link_descriptions_links:
        new_tuple = (link_description[0], link_description[1])
        resulting_tuples.append(new_tuple)
    return resulting_tuples

# images
# r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

# regular links
# r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


def split_nodes_image(old_nodes):
    # helperfunctions for readability, not tested
    def new_textnode(text):
        return TextNode(text, TextType.TEXT)
    def new_image_node(description_link):
        return TextType(description_link[0], TextType.IMAGE, description_link[1])

    resulting_nodes = []
    extracted_image_links = []
    full_text = ""
    new_text = []
    for node in old_nodes:
        # Step 1, extract all the links in to link list from this node
        current_links = extract_markdown_images(node.get_text())
        # current_links, list of tuples 
        #           [(0,1), (0,1), ...]
        #             [0]    [1]   ... 


        # Step 2, loop over links and 
        for description_link in extracted_image_links:
            # Step 3 - split TEXT at link, leave REST
            # Step 4 - make textnode out of first entry
            # Step 5 - include link/image_node
            # Step 6 - append to resulting_nodes

            # Step 7- TEXT = REST
            pass
        # ... Step 2
        
    return resulting_nodes





def split_nodes_link(old_nodes):
    # helperfunctions for readility
    def new_textnode(text): # not tested
        return TextNode(text, TextType.TEXT)
    def new_link_node(description_link): # not tested
        return TextType(description_link[0], TextType.LINK, description_link[1])
    pass