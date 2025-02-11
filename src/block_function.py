import re

from functions import text_to_textnodes

def block_to_block_type(block: str):
    if is_heading(block):
        return "heading"
    if is_code(block):
        return "code"
    if is_quote(block):
        return "quote"
    if is_unordered_list(block):
        return "unordered_list"
    if is_ordered_list(block):
        return "ordered_list"
    return "paragraph"

def is_heading(block: str):
    if re.match(r"^#{1,6} (.*)", block):
        return True
    return False

def is_code(block: str):
    if re.match(r"(?s)^`{3}(.*?)`{3}$", block):
        return True
    return False

def is_quote(block: str):
    lines = block.split('\n')
    return all(line.startswith('>') for line in lines)

def is_unordered_list(block: str):
    lines = block.split('\n')
    # Skip empty lines and the first line if it doesn't start with a marker
    content_lines = [line for line in lines if line.strip()]
    if not content_lines:
        return False
    return any(line.strip().startswith(('* ', '- ')) for line in content_lines)

def is_ordered_list(block: str):
    lines = block.split('\n')
    number = 0
    if all(re.match(r"^\d+\.\s", line) for line in lines):
        for line in lines:
            number_part = line.split('.')[0]
            if int(number_part) != number + 1:
                return False
            number = int(number_part)
        return True
    return False

def extract_text_from_block(block: str, block_type: str):
    match block_type:
        case "paragraph":
            return text_to_textnodes(block)
        case "heading":
            text = re.findall(r"^#{1,6} (.*)", block)[0]
            return text_to_textnodes(text)
        case "quote":
            text = re.sub('> ', '', block)
            return text_to_textnodes(text)
        case "unordered_list":
            text = re.sub(r'\* ', '', block)
            text = re.sub(r'\- ', '', text)
            return text_to_textnodes(text)
        case "ordered_list":
            text = re.sub(r'^\d+\.\s', '', block)
            return text_to_textnodes(text)
        case _:
            raise ValueError(f"unknown format: {block_type}")
        
def extract_code_block(block: str):
    return re.findall(r"(?s)^`{3}(.*?)`{3}$", block)[0]