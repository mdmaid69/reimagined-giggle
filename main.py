import datetime
def get_today_date():
        return datetime.date.today()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)