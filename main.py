import datetime
def get_today_date():
        return datetime.date.today()
import os
def change_working_directory(path):
        os.chdir(path)