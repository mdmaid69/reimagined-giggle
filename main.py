import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import datetime
def get_today_date():
        return datetime.date.today()