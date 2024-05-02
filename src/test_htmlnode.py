import unittest

from htmlnode import HTMLNode
from htmlnode import ParentNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode('p', 'silly goose', ['a', 'b', 'c'], {'target': 'blank'})
        self.assertEqual(node.__repr__(), "HTMLNode(tag=p, value=silly goose, children=['a', 'b', 'c'], props={'target': 'blank'})")

    def test_none(self):
        node = HTMLNode()
        self.assertEqual(node.__repr__(), "HTMLNode(tag=None, value=None, children=None, props=None)")

    def test_leafnode(self):
        node = LeafNode('this is a node', {'target': 'blank'}, tag='p')
        self.assertEqual(node.to_html(), '<p target="blank" >this is a node</p>')

    def test_parentnode(self):
        childnode = LeafNode('this is a node', {'target': 'blank'}, tag='p')
        childnode2 = LeafNode('this is another node', {'src': 'pic.jpg'}, tag='img')

        node = ParentNode(tag='div', children=[childnode, childnode2], props={'class': 'content'})
        self.assertEqual(node.to_html(), '<div class="content" ><p target="blank" >this is a node</p><img src="pic.jpg" >this is another node</img></div>')

    def test_parentnode_repr(self):
        childnode = LeafNode('this is a node', {'target': 'blank'}, tag='p')
        childnode2 = LeafNode('this is another node', {'src': 'pic.jpg'}, tag='img')

        node = ParentNode(tag='div', children=[childnode, childnode2], props={'class': 'content'})
        self.assertEqual(node.__repr__(), f'ParentNode(div, children: [{childnode.__repr__()}, {childnode2.__repr__()}]' + ", {'class': 'content'})")

if __name__ == "__main__":
    unittest.main()
