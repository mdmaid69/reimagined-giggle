import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import datetime
def get_current_date():
        return datetime.date.today()