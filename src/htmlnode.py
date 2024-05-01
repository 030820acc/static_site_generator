class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('not complete')

    def props_to_html(self):
        return_string = " "
        for prop in self.props:
            return_string += f"{prop}=\"{self.props[prop]}\" "
        return return_string

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value, props=None, tag=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        return_string = ""
        if self.tag != None:
            return_string += f'<{self.tag}'
        if self.props != None:
            return_string += f'{super().props_to_html()}>'
        return_string += self.value
        if self.tag != None:
            return_string += f'</{self.tag}>'
        return return_string


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        pass