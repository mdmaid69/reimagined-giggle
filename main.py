import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)