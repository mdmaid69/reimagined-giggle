  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))