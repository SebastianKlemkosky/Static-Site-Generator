
from gencontent import generate_page,generate_pages_recursive
import os, shutil

def copy_from_source_to_destination(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination, exist_ok=True)
    copy_recursive(source, destination)

def copy_recursive(source, destination):
    os.makedirs(destination, exist_ok=True)
    contents = os.listdir(source)
    
    for item in contents:
        path = os.path.join(source, item)
        if os.path.isfile(path):
            print(f"Copied: {path}")
            shutil.copy(path,destination)
        else:
            directory_path = os.path.join(destination, item)
            copy_recursive(os.path.join(source,item), directory_path)
            
def main():
    copy_from_source_to_destination("static", "public")
    generate_pages_recursive("content", "template.html", "public")
        
        
if __name__ == "__main__":
    main()