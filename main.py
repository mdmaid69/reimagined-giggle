import time
def get_time_since_epoch():
        return time.time()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)