import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)