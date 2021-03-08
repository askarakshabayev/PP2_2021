import os

def show_files_and_dirs(dir_path: str):
    with os.scandir(dir_path) as scan:
        for entry in scan:
            if entry.is_dir():
                print(entry)

def get_dirs(dir_path: str):
    subfolders = [f.path for f in os.scandir(dir_path) if f.is_dir()]
    return subfolders

def walk(dir_path):
    for root, dirs, files in os.walk(dir_path):
        print(root)
        print(dirs)
        print(files)

# Example 1
# show_files_and_dirs('/Users/askar/Documents/KBTU/PP2/')

# Example 2
# folders = get_dirs('/Users/askar/Documents/KBTU/PP2/')
# print(folders)

# Example 3
walk('/Users/askar/Documents/KBTU/PP2/')
