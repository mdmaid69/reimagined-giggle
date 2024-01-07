  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import random
def generate_random_number(start, end):
        return random.randint(start, end)