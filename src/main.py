
from gencontent import generate_pages_recursive
import os, shutil, sys

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
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    copy_from_source_to_destination("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)
        
        
if __name__ == "__main__":
    main()