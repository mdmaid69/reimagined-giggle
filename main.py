  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import random
def generate_random_sample(population, k):
        return random.sample(population, k)