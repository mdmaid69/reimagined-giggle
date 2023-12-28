import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())