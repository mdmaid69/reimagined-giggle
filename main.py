import time
def get_current_time():
        return time.ctime()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)