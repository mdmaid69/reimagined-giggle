  import os
  def split_path(path):
        return os.path.split(path)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"