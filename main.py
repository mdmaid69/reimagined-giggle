import os
print(os.getcwd())
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)