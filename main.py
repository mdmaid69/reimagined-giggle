import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)