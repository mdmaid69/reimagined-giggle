  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"