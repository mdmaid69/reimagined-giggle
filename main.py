import time
def get_current_time():
        return time.ctime()
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)