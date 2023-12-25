import time
def get_current_time():
        return time.ctime()
import glob
def find_files(pattern):
        return glob.glob(pattern)