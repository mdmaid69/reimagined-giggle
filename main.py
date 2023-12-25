import datetime
def get_current_datetime():
        return datetime.datetime.now()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)