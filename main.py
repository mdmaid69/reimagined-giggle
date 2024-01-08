import datetime
print(datetime.datetime.now())
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)