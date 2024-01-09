import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"