import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"