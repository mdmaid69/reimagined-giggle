import datetime
def get_current_datetime():
        return datetime.datetime.now()
import os
def change_working_directory(path):
        os.chdir(path)