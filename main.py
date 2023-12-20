import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"