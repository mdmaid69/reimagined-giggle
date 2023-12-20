import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)