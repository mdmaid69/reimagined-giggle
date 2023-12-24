import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import datetime
def get_today_date():
        return datetime.date.today()