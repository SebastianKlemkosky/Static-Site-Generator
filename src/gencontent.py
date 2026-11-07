from markdown_blocks import markdown_to_html_node
import os 
import shutil

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("No h1 header")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, encoding="utf-8") as f:
        from_contents = f.read()
        
    with open(template_path, encoding="utf-8") as f:
        template_contents = f.read()
    
    from_html_node = markdown_to_html_node(from_contents)
    from_html_node_str = from_html_node.to_html()
    from_title = extract_title(from_contents)
    
    final_html = template_contents.replace("{{ Title }}", from_title).replace("{{ Content }}", from_html_node_str)
    final_html = final_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    
    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)
    contents = os.listdir(dir_path_content)
    
    
    for item in contents:
        path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(path) and path.endswith(".md"):
            dest_path = dest_path.replace(".md", ".html")
            print(f"File: {dest_path}")
            generate_page(path, template_path, dest_path, basepath)

        elif os.path.isdir(path):
            print(f"Directory: {path}")
            generate_pages_recursive(path, template_path, dest_path, basepath)
                        