  import os
  def get_current_directory():
        return os.getcwd()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)