import time
def get_time_since_epoch():
        return time.time()
import os
def change_working_directory(path):
        os.chdir(path)