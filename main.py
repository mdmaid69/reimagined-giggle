import shutil
def delete_directory(path):
        shutil.rmtree(path)
import os
def get_file_size(filename):
        return os.path.getsize(filename)