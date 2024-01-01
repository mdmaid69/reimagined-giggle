import os
def remove_directory(path):
        os.rmdir(path)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())