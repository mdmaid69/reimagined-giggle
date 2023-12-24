import datetime
def get_today_date():
        return datetime.date.today()
import os
def remove_directory(path):
        os.rmdir(path)