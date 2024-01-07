import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import os
def change_working_directory(path):
        os.chdir(path)