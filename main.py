import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()