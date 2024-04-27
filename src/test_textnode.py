import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', 'bold')
        node2 = TextNode('This is a text node', 'bold')
        self.assertEqual(node, node2)

    def test_eq_method(self):
        node = TextNode('test test test', 'bold')
        node2 = TextNode('test test test', 'bold')
        node3 = TextNode('test Test test test', 'italic')
        node4 = TextNode('test test test', 'italic')
        node5 = TextNode('test', 'bold')
        self.assertEqual(node.__eq__(node2), True)
        self.assertEqual(node.__eq__(node3), False)
        self.assertEqual(node.__eq__(node4), False)
        self.assertEqual(node.__eq__(node5), False)

    def test_repr(self):
        node = TextNode('test', 'bold')
        node2 = TextNode('test', 'bold', 'google.com')
        self.assertEqual(node.__repr__(), 'TextNode(test, bold, None)')
        self.assertEqual(node2.__repr__(), 'TextNode(test, bold, google.com)')


if __name__ == "__main__":
    unittest.main()
