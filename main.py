import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import os
def get_current_working_directory():
        return os.getcwd()