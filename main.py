import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"