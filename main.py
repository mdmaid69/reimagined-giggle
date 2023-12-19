  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import random
def generate_random_sample(population, k):
        return random.sample(population, k)