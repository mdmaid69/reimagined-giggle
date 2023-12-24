import shutil
def delete_directory(path):
        shutil.rmtree(path)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)