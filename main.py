  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import random
def generate_random_sample(population, k):
        return random.sample(population, k)