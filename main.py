import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"