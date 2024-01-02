import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import os
def change_working_directory(path):
        os.chdir(path)