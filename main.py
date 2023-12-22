import os
def change_working_directory(path):
        os.chdir(path)
import time
def get_current_time():
        return time.ctime()