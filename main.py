import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import time
def get_current_time():
        return time.ctime()