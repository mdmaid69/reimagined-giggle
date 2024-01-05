  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))