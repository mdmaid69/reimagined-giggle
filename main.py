import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import os
def get_file_size(filename):
        return os.path.getsize(filename)