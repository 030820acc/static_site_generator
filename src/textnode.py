from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode):
        return (self.text == textnode.text
                and self.text_type == textnode.text_type
                and self.url == textnode.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    if text_node.text_type == 'bold':
        return LeafNode(tag='b', value=text_node.text)
    if text_node.text_type == 'italic':
        return LeafNode(tag='i', value=text_node.text)
    if text_node.text_type == 'code':
        return LeafNode(tag='code', value=text_node.text)
    if text_node.text_type == 'link':
        return LeafNode(tag='a', value=text_node.text, props={'href': text_node.url})
    if text_node.text_type == 'image':
        return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
    raise Exception('textnode does not have a valid text type')