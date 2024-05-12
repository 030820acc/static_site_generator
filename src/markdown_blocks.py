import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    line_list = markdown.split("\n\n")
    filtered_list = filter(lambda x: len(x) > 0, line_list)
    trimmed_filtered_list = list(map(lambda x: x.strip(' '), filtered_list))
    return trimmed_filtered_list

def block_to_block_type(block):
    if re.match(r"(#{1,6} )", block) != None: 
        return block_type_heading
    elif re.match(r"^(```[^`])", block) != None:
        return block_type_code
    elif re.match(r"^>[^>]", block) != None:
        return block_type_quote
    elif re.match(r"^(\* )", block) != None or re.match(r"^(- )", block) != None:
        return block_type_unordered_list
    elif re.match(r"^(\d+\. )", block) != None:
        return block_type_ordered_list
    else:
        return block_type_paragraph