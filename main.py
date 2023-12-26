import time
def get_current_time():
        return time.time()
import os
def remove_directory(path):
        os.rmdir(path)