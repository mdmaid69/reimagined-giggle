import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)