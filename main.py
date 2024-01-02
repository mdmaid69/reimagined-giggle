import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import time
def get_current_time():
        return time.time()