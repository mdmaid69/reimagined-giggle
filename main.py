import time
def get_time_since_epoch():
        return time.time()
import os
def remove_directory(path):
        os.rmdir(path)