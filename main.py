  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)