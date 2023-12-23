import datetime
def get_current_datetime():
        return datetime.datetime.now()
import glob
def find_files(pattern):
        return glob.glob(pattern)