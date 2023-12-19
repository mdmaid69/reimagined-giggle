import os
def get_current_working_directory():
        return os.getcwd()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)