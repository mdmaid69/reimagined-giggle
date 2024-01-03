import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import datetime
def get_today_date():
        return datetime.date.today()