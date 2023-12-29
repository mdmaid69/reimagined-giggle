import os
def remove_directory(path):
        os.rmdir(path)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)