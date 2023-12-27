import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"