from htmlnode import (
    ParentNode,
    LeafNode,
    HTMLNode,

)

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type
)

from inline_markdown import text_to_textnodes

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
        count = 0
        for i in range(0, len(line)):
            if line[i] == "#":
                count += 1
        children_nodes.append(LeafNode(f"h{count}", line.strip("# ")))
    return children_nodes

def markdown_to_htmlnode(md):
    children_nodes = []
    markdown_blocks = markdown_to_blocks(md)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == "ordered_list":
            children_nodes.extend(ordered_block_to_html(block))
        if block_type == "unordered_list":
            children_nodes.extend(unordered_block_to_html(block))
        if block_type == "quote":
            children_nodes.extend(quote_block_to_html(block))
        if block_type == "heading":
            children_nodes.extend(heading_block_to_html(block))
        if block_type == "code":
            children_nodes.extend(code_block_to_html(block))
        if block_type == "paragraph":
            children_nodes.extend(text_to_textnodes(block))
    wrapper = ParentNode("div", children_nodes)
    return wrapper