  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"