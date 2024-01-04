  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"