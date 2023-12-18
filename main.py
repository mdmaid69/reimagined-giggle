import time
def get_current_time():
        return time.time()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)