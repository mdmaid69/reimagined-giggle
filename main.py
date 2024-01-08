import datetime
def get_current_datetime():
        return datetime.datetime.now()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)