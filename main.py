import time
def get_current_time():
        return time.ctime()
import re
def split_string(pattern, string):
        return re.split(pattern, string)