import os
def remove_directory(path):
        os.rmdir(path)
import os
def list_files_in_directory(path):
        return os.listdir(path)