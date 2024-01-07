import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)