import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)