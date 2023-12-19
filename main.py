import random
def roll_die():
        return random.randint(1, 6)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)