from textnode import TextType

DELIMITERS = [("**", TextType.BOLD), ("*", TextType.ITALIC), ("`", TextType.CODE)]
BLOCK_TYPE = ["heading", "code", "quote", "unordered_list", "ordered_list", "paragraph"]