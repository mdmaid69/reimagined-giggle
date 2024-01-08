import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import shutil
def delete_directory(path):
        shutil.rmtree(path)