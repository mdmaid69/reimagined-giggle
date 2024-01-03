import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)