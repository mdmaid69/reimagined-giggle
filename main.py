import os
def get_file_size(filename):
        return os.path.getsize(filename)
import os
def change_working_directory(path):
        os.chdir(path)