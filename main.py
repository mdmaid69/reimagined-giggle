import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import datetime
def get_current_datetime():
        return datetime.datetime.now()