import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import time
def get_current_time():
        return time.time()