import datetime
def get_current_datetime():
        return datetime.datetime.now()
import os
def remove_directory(path):
        os.rmdir(path)