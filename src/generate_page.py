import os
from markdown_to_html import markdown_to_html_node

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)

    for item in items:
        source_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(source_path):
            dest_path = dest_path.replace('.md', '.html')
            generate_page(source_path, template_path, dest_path)
        else:
            generate_page_recursive(source_path, template_path, dest_path)
        


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path) as f:
        markdown_src = f.read()
    with open(template_path) as f:
        template = f.read()
    
    title = extract_title(markdown_src)
    content = markdown_to_html_node(markdown_src).to_html()
    template = template.replace(' {{ Title }} ', '{{ Title }}')
    html = template.replace('{{ Title }}', title)
    html = html.replace('{{ Content }}', content)


    # Make sure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the final HTML to the destination
    with open(dest_path, 'w') as f:
        f.write(html)


def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            # Remove the '# ' and any extra whitespace
            return line[2:].strip()
    raise Exception('No h1 header found')