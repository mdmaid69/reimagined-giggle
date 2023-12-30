import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)