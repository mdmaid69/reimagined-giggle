  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"