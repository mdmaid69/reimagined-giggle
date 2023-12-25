import os
def remove_directory(path):
        os.rmdir(path)
import shutil
def delete_directory(path):
        shutil.rmtree(path)