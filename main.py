import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import shutil
def delete_directory(path):
        shutil.rmtree(path)