import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import time
def get_current_time():
        return time.ctime()