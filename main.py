import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import os
def remove_directory(path):
        os.rmdir(path)