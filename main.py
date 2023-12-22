import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())