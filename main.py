  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import itertools
print(list(itertools.permutations([1, 2, 3])))