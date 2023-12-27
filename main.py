  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)