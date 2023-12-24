import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import os
def remove_directory(path):
        os.rmdir(path)