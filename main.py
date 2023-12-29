  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"