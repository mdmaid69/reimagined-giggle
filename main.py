import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def get_directory_name(path):
        return os.path.dirname(path)