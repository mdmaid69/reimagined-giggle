import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import os
def list_files_in_directory(path):
        return os.listdir(path)