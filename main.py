import datetime
def get_today_date():
        return datetime.date.today()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)