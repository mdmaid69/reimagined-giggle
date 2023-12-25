import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)