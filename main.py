import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import datetime
def get_current_datetime():
        return datetime.datetime.now()