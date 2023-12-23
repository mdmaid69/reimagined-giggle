import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())