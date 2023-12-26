import os
def remove_directory(path):
        os.rmdir(path)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)