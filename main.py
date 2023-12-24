import re
def split_string(pattern, string):
        return re.split(pattern, string)
import time
def get_time_since_epoch():
        return time.time()