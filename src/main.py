from textnode import TextNode, TextType
import os
import shutil

def main():
    clear_public()
    copy_content_to_public("./static")

def clear_public():
    public_dir = "./public"
    if os.path.exists(public_dir):
        print(f"Deleting dir {public_dir}")
        shutil.rmtree(public_dir)

def copy_content_to_public(dir, dst = "./public"):
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
main()