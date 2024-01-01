import time
def get_time_since_epoch():
        return time.time()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)