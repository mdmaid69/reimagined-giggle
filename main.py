import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import os
  def get_base_name(path):
        return os.path.basename(path)