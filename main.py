import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks