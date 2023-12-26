import os
def change_working_directory(path):
        os.chdir(path)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)