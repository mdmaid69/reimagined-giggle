import os
def get_file_size(filename):
        return os.path.getsize(filename)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)