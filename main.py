import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import datetime
def get_current_datetime():
        return datetime.datetime.now()