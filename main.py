import time
def get_current_time():
        return time.time()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)