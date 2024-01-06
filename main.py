  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)