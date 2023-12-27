import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import os
def change_working_directory(path):
        os.chdir(path)