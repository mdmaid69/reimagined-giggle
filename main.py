  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import random
def generate_random_sample(population, k):
        return random.sample(population, k)