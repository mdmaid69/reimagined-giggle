  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)