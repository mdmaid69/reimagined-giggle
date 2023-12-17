import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"