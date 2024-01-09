import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize