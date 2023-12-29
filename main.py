import datetime
def get_current_date():
        return datetime.date.today()
import re
def split_string(pattern, string):
        return re.split(pattern, string)