import os
def change_working_directory(path):
        os.chdir(path)
import shutil
def delete_directory(path):
        shutil.rmtree(path)