import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import time
def get_time_since_epoch():
        return time.time()