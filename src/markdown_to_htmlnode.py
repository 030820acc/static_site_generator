from htmlnode import (
    ParentNode,
    LeafNode,
    HTMLNode,

)

def quote_block_to_html(block):
    md_lines = block.split("\n")
    stripped_lines = []
    for line in md_lines:
        line.strip("<")
    return LeafNode("blockquote", "\n".join(stripped_lines))

def code_block_to_html(block):
    stripped_block = block.strip('`')
    code_node = LeafNode("code", stripped_block)
    return ParentNode("pre", [code_node])

def unordered_block_to_html(block):
    md_lines = block.split("\n")
    children_nodes = []
    for line in md_lines:
        children_nodes.append(LeafNode("li", line.strip("*- ")))
    return ParentNode("ul", children_nodes)

def ordered_block_to_html(block):
    md_lines = block.split("\n")
    children_nodes = []
    for line in md_lines:
        node = LeafNode("li", " ".join(line.split(' ')[1:]))
        children_nodes.append(node)
    return ParentNode('ol', children_nodes)

def heading_block_to_html(block):
    md_lines = block.split("\n")
    children_nodes = []
    for line in md_lines:
        children_nodes.append(LeafNode("")) # unfinished

def markdown_to_htmlnode(md):
    children_nodes = []

    wrapper = ParentNode("div", children_nodes)