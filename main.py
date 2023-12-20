import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import os
def list_files_in_directory(path):
        return os.listdir(path)