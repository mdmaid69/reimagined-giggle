  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)