import datetime
def get_current_datetime():
        return datetime.datetime.now()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)