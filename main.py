import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import glob
def find_files(pattern):
        return glob.glob(pattern)