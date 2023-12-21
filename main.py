import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)