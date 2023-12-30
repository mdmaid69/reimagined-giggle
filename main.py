import datetime
def get_current_date():
        return datetime.date.today()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)