import os
def get_current_working_directory():
        return os.getcwd()
import shutil
def delete_directory(path):
        shutil.rmtree(path)