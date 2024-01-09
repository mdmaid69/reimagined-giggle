  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))