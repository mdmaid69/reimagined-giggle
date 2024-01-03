import random
def generate_random_choice(choices):
        return random.choice(choices)
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev