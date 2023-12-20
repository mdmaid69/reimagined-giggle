import time
def get_current_time():
        return time.time()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)