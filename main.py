import random
def generate_random_choice(choices):
        return random.choice(choices)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)