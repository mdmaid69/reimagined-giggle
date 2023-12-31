  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)