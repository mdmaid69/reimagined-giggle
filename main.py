  import os
  def delete_file(file_name):
        os.remove(file_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"