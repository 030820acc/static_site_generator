import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode('p', 'silly goose', ['a', 'b', 'c'], {'target': 'blank'})
        self.assertEqual(node.__repr__(), "HTMLNode(tag=p, value=silly goose, children=['a', 'b', 'c'], props={'target': 'blank'})")

    def test_none(self):
        node = HTMLNode()
        self.assertEqual(node.__repr__(), "HTMLNode(tag=None, value=None, children=None, props=None)")


if __name__ == "__main__":
    unittest.main()
