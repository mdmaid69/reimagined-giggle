import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())