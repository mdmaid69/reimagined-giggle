import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)