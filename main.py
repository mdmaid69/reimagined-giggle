import os
print(os.getcwd())
import shutil
def move_file(src, dst):
        shutil.move(src, dst)