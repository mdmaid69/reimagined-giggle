  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)