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
    def make_textnode(text):
        return TextNode(text, TextType.TEXT)
    def make_image_node(description_link):
        print(description_link[0], type(description_link[0]))
        print(description_link[1], type(description_link[1]))
        return TextNode(description_link[0], TextType.IMAGE, description_link[1])

    resulting_nodes = []

    for _, node in enumerate(old_nodes):
        current_text = node.get_text()
        # Step 1, extract all the links in to link list from this node
        all_links_of_node = extract_markdown_images(current_text)
        # all_links_of_node, list of tuples 
        #           [(0,1), (0,1), ...]
        #             [0]    [1]   ...
        # Step 2, loop over links and 
        for _, description_link in enumerate(all_links_of_node):
            image_alt = description_link[0]
            image_link = description_link[1]
            # Step 3 - split TEXT at link, leave REST
            textnode_rest_pair = current_text.split(f"![{image_alt}]({image_link})", 1)
            # textnode_rest_pair, list of two strings
            # ["text to textnode", "rest text to peruse for links"]
            #  textnode_rest_pair[0] textnode_rest_pair[1] 

            # Step 4 - make textnode out of first entry
            new_textnode = make_textnode(textnode_rest_pair[0])
            # Step 5 - make link/image_node
            new_image_node = make_image_node(description_link)
            # Step 6 - append botg to resulting_nodes
            resulting_nodes.append(new_textnode)
            resulting_nodes.append(new_image_node)
            # Step 7 - TEXT = REST, update current_text to rest
            current_text = textnode_rest_pair[1]
        # ... Step 2
            # Step 8, if rest (= current text) not empty, make textnode and append
        if len(current_text) > 0:
            resulting_nodes.append(TextNode(current_text, TextType.TEXT))
        

    return resulting_nodes





def split_nodes_link(old_nodes):
    # helperfunctions for readility
    def make_textnode(text): # not tested
        return TextNode(text, TextType.TEXT)
    def make_link_node(description_link): # not tested
        return TextNode(description_link[0], TextType.LINK, description_link[1])
    
    resulting_nodes = []
    for node in old_nodes:
        current_text = node.get_text()
        # Step 1, extract all the links in to link list from this node
        all_links_of_node = extract_markdown_links(current_text)
        # all_links_of_node, list of tuples 
        #           [(0,1), (0,1), ...]
        #             [0]    [1]   ...
        # Step 2, loop over links and 
        for description_link in all_links_of_node:
            link_alt = description_link[0]
            link_link = description_link[1]
            # Step 3 - split TEXT at link, leave REST
            textnode_rest_pair = current_text.split(f"[{link_alt}]({link_link})", 1)
            # textnode_rest_pair, list of two strings
            # ["text to textnode", "rest text to peruse for links"]
            #  textnode_rest_pair[0] textnode_rest_pair[1]  
                    
            # Step 4 - make textnode out of first entry
            new_textnode = make_textnode(textnode_rest_pair[0])
            # Step 5 - make link/image_node
            new_link_node = make_link_node(description_link)
            # Step 6 - append botg to resulting_nodes
            resulting_nodes.append(new_textnode)
            resulting_nodes.append(new_link_node)
            # Step 7 - TEXT = REST, update current_text to rest
            current_text = textnode_rest_pair[1]
        # ... Step 2
        # Step 8, if rest (= current text) not empty, make textnode
        if len(current_text) > 0:
            resulting_nodes.append(TextNode(current_text, TextType.TEXT))
        
    return resulting_nodes


def text_to_textnodes(text):
    """
    text:
        markdown formated string
    return:
        list of textnodes, each with corresponding texttype, formatting, etc.

    """
    resulting_nodes = []
    # make a node out of the initial text input
    raw_node = TextNode(text, TextType.TEXT)
    # split into nodes:
    # BOLD, TEXT, ITALIC, TEXT, ITALIC, CODE etc...
    links_images_not_extracted = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([raw_node], "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE)
    # NOW: TEXT nodes still possibly contain LINKS or IMAGE
    for node in links_images_not_extracted:
        # if the node is not TEXT we can just append it
        print("I am a node of type: ", type(node))
        if node.get_text_type() != TextType.TEXT:
            resulting_nodes.append(node)
        # otherwise it is TEXT and might contain LINK or IMAGE
        else:
            # Let us extract the links
            image_not_extracted = split_nodes_link([node])
            # now we have a list
            # [TEXT, LINK, TEXT, LINK]
            # list of textnodes, TextTypes: LINK, TEXT, LINK, TEXT
            # apply split_nodes_image to remaining TextType.TEXT nodes
            link_image_extracted = []
            for current in image_not_extracted:
                if current.get_text_type() == TextType.LINK:
                    # if node is LINK, append
                    link_image_extracted.append(current)
                else:
                    # node is TEXT and might contain IMAGE
                    link_image_extracted.append(split_nodes_image([current]))
                    # appends TEXT, IMAGE TEXT
                    # or TEXT
                    # or IMAGE, IMAGE etc
            # if last node was ITALIC, resulting nodes looks like
            # [..., ITALIC]
            # now we append eg [TEXT, IMAGE, LINK, TEXT]
            # [..., ITALIC, TEXT, IMAGE, LINK, TEXT]
            resulting_nodes.append(link_image_extracted)
            # and go to next node that will be either TEXT to repeat unpacking, or
            # ITALIC, CODE, BOLD and will just be appended
    return resulting_nodes