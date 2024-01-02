import os
def change_working_directory(path):
        os.chdir(path)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())