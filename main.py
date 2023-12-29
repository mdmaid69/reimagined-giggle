  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))