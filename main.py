import datetime
def get_current_datetime():
        return datetime.datetime.now()
import re
def split_string(pattern, string):
        return re.split(pattern, string)