import datetime
def get_today_date():
        return datetime.date.today()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)