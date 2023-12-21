  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)