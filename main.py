import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  def is_even(n):
        return n % 2 == 0