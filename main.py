import time
def get_current_time():
        return time.time()
import os
def get_file_size(filename):
        return os.path.getsize(filename)