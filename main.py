import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)