import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r