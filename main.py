import os
def get_file_size(filename):
        return os.path.getsize(filename)
import datetime
def get_current_datetime():
        return datetime.datetime.now()