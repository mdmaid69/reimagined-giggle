import random
def generate_random_choice(choices):
        return random.choice(choices)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink