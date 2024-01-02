import datetime
def get_today_date():
        return datetime.date.today()
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)