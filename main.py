  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)