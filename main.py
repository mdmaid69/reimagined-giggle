import time
def get_time_since_epoch():
        return time.time()
import glob
def find_files(pattern):
        return glob.glob(pattern)