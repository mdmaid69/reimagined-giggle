import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)