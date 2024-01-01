  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"