import datetime
def get_current_date():
        return datetime.date.today()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)