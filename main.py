import time
def get_current_time():
        return time.time()
import glob
def find_files(pattern):
        return glob.glob(pattern)