import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)