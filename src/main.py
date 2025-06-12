from textnode import TextNode, TextType
import os
import shutil
import sys
from markdownconverter import markdown_to_html_node

basepath = ""
if len(sys.argv) > 1:
    basepath = sys.argv[1] + "/"

def main():
    clear_public()
    print("================")
    copy_content_to_public("./static")
    print("================")
    #generate_page("./content/index.md", "./template.html", "./public/index.html")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

def clear_public():
    public_dir = "./docs"
    if os.path.exists(public_dir):
        print(f"Deleting dir {public_dir}")
        shutil.rmtree(public_dir)

def copy_content_to_public(dir, dst = "./docs"):
    # shutil.copytree() exists but is not to be used for the course
    if not os.path.exists(dir):
        raise ValueError("Dir does not exist")
    print(f"Copying {dir} to public")
    if not os.path.exists(dst):
        print(f"Creating dir {dst}")
        os.mkdir(dst)
    files = os.listdir(dir)
    for file in files:
        file_path = os.path.join(dir, file)
        if os.path.isdir(file_path):
            print(f"{file} is a dir, recursive call")
            copy_content_to_public(file_path, os.path.join(dst, file))
        else:
            print(f"Copying {file_path} to {dst}")
            shutil.copy(file_path, os.path.join(dst, file))

def extract_title(markdown):
    lines = markdown.split('\n')
    title = None
    for line in lines:
        split = line.split("# ")
        if split[0] == "":
            title = split[1]
            break
    if title == None:
        raise ValueError("No h1 header was found for title")
    return title

def generate_page(src, tem, dst, basepath):
    print(f"Generating page from {src} to {dst} using {tem} as a template.")
    # if destination dir doesn't exist create it
    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    if os.path.exists(src) and os.path.exists(tem):
        with open(src) as s:
            with open(tem) as t:
                md = s.read()
                title = extract_title(md)
                template = t.read()
                node = markdown_to_html_node(md)
                html = node.to_html()
                page = template.replace("{{ Content }}", html).replace("{{ Title }}", title)
                links = page.replace("href=\"/", f"href=\"/{basepath}").replace("src=\"/", f"src=\"/{basepath}")
                with open(dst, 'w') as d:
                    d.write(links)

def generate_pages_recursive(src, tem, dst, basepath):
    if os.path.exists(src):
        files = os.listdir(src)
        for file in files:
            file_path = os.path.join(src, file)
            if os.path.isdir(file_path):
                generate_pages_recursive(file_path, tem, os.path.join(dst, file), basepath)
            else:
                file_name = '.'.join(file.split('.')[:-1])
                if file.split('.')[-1] == "md":
                    generate_page(file_path, tem, os.path.join(dst, f"{file_name}.html"), basepath)
main()