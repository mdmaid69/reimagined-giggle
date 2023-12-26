import os
def remove_directory(path):
        os.rmdir(path)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)