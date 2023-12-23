import time
def get_current_time():
        return time.ctime()
import os
def list_files_in_directory(path):
        return os.listdir(path)