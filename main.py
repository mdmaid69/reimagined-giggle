import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import datetime
def get_current_datetime():
        return datetime.datetime.now()