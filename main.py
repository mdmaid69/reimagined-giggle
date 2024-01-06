import os
def remove_directory(path):
        os.rmdir(path)
import time
def get_current_time():
        return time.ctime()