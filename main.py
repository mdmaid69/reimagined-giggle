import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)