import time
def get_current_time():
        return time.ctime()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)