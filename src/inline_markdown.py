from textnode import (
    TextNode,
    text_type_text
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        string_list = node.text.split(delimiter)
        if len(string_list) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(string_list)):
            if string_list[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(string_list[i], text_type_text))
            else:
                split_nodes.append(TextNode(string_list[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes