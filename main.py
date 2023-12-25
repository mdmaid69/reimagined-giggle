import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)