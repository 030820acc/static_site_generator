from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link
)

import re


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


def split_nodes_image(old_nodes):
    fixed_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            fixed_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) < 1:
            fixed_nodes.append(node)
            continue
        node_var = node.text
        for image in images:
            splits = node_var.split(f"![{image[0]}]({image[1]})")
            if len(splits) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if splits[0] != '':
                fixed_nodes.append(TextNode(splits[0], text_type_text))
            fixed_nodes.append(TextNode(image[0], text_type_image, image[1]))
            node_var = splits[1]
        if node_var != '':
            fixed_nodes.append(TextNode(node_var, text_type_text))
    return fixed_nodes


def split_nodes_link(old_nodes):
    fixed_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            fixed_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) < 1:
            fixed_nodes.append(node)
            continue
        node_var = node.text
        for link in links:
            splits = node_var.split(f"[{link[0]}]({link[1]})")
            if len(splits) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if splits[0] != '':
                fixed_nodes.append(TextNode(splits[0], text_type_text))
            fixed_nodes.append(TextNode(link[0], text_type_link, link[1]))
            node_var = splits[1]
        if node_var != '':
            fixed_nodes.append(TextNode(node_var, text_type_text))
    return fixed_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text) 


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)     


def text_to_textnodes(text):
    pass