import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import os
def list_files_in_directory(path):
        return os.listdir(path)