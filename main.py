  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)