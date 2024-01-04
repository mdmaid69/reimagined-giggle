import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"