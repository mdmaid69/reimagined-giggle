import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import os
def list_files_in_directory(path):
        return os.listdir(path)