import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)