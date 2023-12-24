import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import datetime
def get_today_date():
        return datetime.date.today()