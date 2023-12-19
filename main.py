  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)