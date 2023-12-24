  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import collections
def count_elements(iterable):
        return collections.Counter(iterable)