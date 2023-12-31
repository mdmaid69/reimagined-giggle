import datetime
def get_current_date():
        return datetime.date.today()
import os
def list_files_in_directory(path):
        return os.listdir(path)