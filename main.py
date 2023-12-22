  import os
  def get_base_name(path):
        return os.path.basename(path)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"