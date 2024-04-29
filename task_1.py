import os
from os import path
import shutil


def dir_copy(src, dest='dist'):
    try:
        src = path.abspath(src)
        dest = path.abspath(dest)
        if not path.exists(dest):
            os.mkdir(dest)
        for item in os.listdir(src):
            rel_path = path.abspath(path.join(src, item))
            rel_path = rel_path.replace(src, '')
            if path.isdir(src + rel_path):
                dir_copy(src + rel_path, dest + rel_path)
            else:
                shutil.copy(src + rel_path, dest + rel_path)
            print(f'Copied {item} to {dest}')

    except Exception as err:
        print(err)


dir_copy('orig')
