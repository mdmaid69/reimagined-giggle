  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"