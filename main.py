import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]