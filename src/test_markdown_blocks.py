import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_ordered_list,
    block_type_quote,
    block_type_unordered_list,
)

class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        test_md = 'This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items'
        self.assertEqual(markdown_to_blocks(test_md), ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"])

    def test_markdown_to_blocks_with_whitespace(self):
        test_md = '      This is **bolded** paragraph      \n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items'
        self.assertEqual(markdown_to_blocks(test_md), ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"])

    def test_block_to_block_type(self):
        test_md = "##heading\n\n```codeblock```\n\n>quotes\n\n* unordered list 1\n\n- unordered list 2\n\n1. ordered list\n\nthis is just a paragraph"
        block_list = markdown_to_blocks(test_md)
        self.assertEqual(block_to_block_type(block_list[0]), "heading")
        self.assertEqual(block_to_block_type(block_list[1]), "code")
        self.assertEqual(block_to_block_type(block_list[2]), "quote")
        self.assertEqual(block_to_block_type(block_list[3]), "unordered_list")
        self.assertEqual(block_to_block_type(block_list[4]), "unordered_list")
        self.assertEqual(block_to_block_type(block_list[5]), "ordered_list")
        self.assertEqual(block_to_block_type(block_list[6]), "paragraph")

if __name__ == "__main__":
    unittest.main()
