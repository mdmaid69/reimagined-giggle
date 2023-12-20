import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"