import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)