import os
def get_file_size(filename):
        return os.path.getsize(filename)
import os
def list_files_in_directory(path):
        return os.listdir(path)