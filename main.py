  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"