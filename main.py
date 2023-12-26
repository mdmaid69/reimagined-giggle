import os
def remove_directory(path):
        os.rmdir(path)
import os
def get_file_size(filename):
        return os.path.getsize(filename)