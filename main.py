import shutil
def delete_directory(path):
        shutil.rmtree(path)
import datetime
def get_today_date():
        return datetime.date.today()