  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)