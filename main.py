import datetime
def get_current_datetime():
        return datetime.datetime.now()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)