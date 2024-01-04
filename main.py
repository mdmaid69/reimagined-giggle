import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"