import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import os
def get_file_size(filename):
        return os.path.getsize(filename)