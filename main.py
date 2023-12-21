import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  def is_odd(n):
        return n % 2 != 0