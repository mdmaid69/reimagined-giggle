import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)