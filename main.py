import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  def is_even(n):
        return n % 2 == 0