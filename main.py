import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)