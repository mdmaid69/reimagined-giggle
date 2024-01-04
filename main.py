import os
def get_file_size(filename):
        return os.path.getsize(filename)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)