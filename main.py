  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)