import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import os
def list_files_in_directory(path):
        return os.listdir(path)