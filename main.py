import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)