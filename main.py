import random
def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)