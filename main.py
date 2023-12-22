  def is_odd(n):
        return n % 2 != 0
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)