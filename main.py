  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import random
def generate_random_sample(population, k):
        return random.sample(population, k)