import os
def get_file_size(filename):
        return os.path.getsize(filename)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())