import os
import fnmatch

dir_path = '/Users/askar/Documents/KBTU/PP2/week5/'

with os.scandir(dir_path) as items:
    for item in items:
        if item.is_file():
            if fnmatch.fnmatch(item.name, "*.py"):
                print(f"________________{item.name}")
                file = open(item.name)
                content = file.read()
                print(content)
                file.close()



