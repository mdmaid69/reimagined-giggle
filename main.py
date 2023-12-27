import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import os
def get_file_size(filename):
        return os.path.getsize(filename)