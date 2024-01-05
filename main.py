import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import os
def list_files_in_directory(path):
        return os.listdir(path)