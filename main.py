import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)