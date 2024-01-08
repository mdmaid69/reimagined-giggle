  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"