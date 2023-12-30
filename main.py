import time
def get_time_since_epoch():
        return time.time()
import os
def get_file_size(filename):
        return os.path.getsize(filename)