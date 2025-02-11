import os
import shutil
from generate_page import generate_page_recursive


def main():      
    copy_static("./static", "./public")
    generate_page_recursive("./content", "./template.html", "./public")

    return

def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
        
    # Get list of all items in source_dir
    items = os.listdir(source_dir)

    for item in items:
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isfile(source_path):
            print(f'file copied from: {source_path}\n to: {dest_path}')
            shutil.copy(source_path, dest_path)
        else:
            copy_static(source_path, dest_path)

main()