import random
def generate_random_choice(choices):
        return random.choice(choices)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)