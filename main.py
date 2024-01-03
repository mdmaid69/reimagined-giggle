  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"