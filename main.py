import datetime
def get_current_date():
        return datetime.date.today()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)