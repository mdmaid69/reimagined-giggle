  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)