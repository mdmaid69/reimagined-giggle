import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import time
def get_current_time():
        return time.ctime()