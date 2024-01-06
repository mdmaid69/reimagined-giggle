import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import time
def get_time_since_epoch():
        return time.time()