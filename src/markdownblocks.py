from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n\n")
    for line in lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")
    # Is heading?
    if lines[0][0] == "#":
        split = lines[0].split(" ")
        # Max # length is 6, more means incorrect markdown.
        if len(split[0]) > 6:
            return BlockType.PARAGRAPH
        has_error = False
        for char in split[0]:
            if not char == "#":
                has_error = True
        if has_error:
            #raise ValueError("Heading starts with non # character")
            return BlockType.PARAGRAPH
        return BlockType.HEADING
    # Is code?
    if lines[0][0] == "`":
        if lines[0][:3] == "```" and lines[-1][-3:] == "```":
            has_error = False
            for line in lines[1:-2]:
                if "```" in line:
                    has_error = True
            if has_error:
                #raise ValueError("Markdown code block is contains closing ``` before end")
                return BlockType.PARAGRAPH
            return BlockType.CODE
    # Is quote?
    if lines[0][0] == ">":
        has_error = False
        for line in lines:
            if not line[0:2] == "> ":
                has_error = True
        if has_error:
            #raise ValueError("A line in markdown quote does not start with '>'")
            return BlockType.PARAGRAPH
        return BlockType.QUOTE
    # Is unordered list?
    if lines[0][0] in "*-":
        has_error = False
        for line in lines:
            if not line[0] in "*-" or not line[1] == " ":
                has_error = True
        if has_error:
            #raise ValueError("Unordered list is not properly formated")
            return BlockType.PARAGRAPH
        return BlockType.U_LIST
    # Is ordered list?
    if lines[0][0] == "1":
        has_error = False
        for i, line in enumerate(lines, 1):
            digits = len(str(i))
            if not int(line[0:digits]) == i or not line[digits:digits+2] == ". ":
                has_error = True
        if has_error:
            #raise ValueError("Ordered list is not properly formated")
            return BlockType.PARAGRAPH
        return BlockType.O_LIST
    # Is none of the above, so paragraph?
    return BlockType.PARAGRAPH