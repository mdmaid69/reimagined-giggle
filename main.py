import time
def get_current_time():
        return time.ctime()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)