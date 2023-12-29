import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)