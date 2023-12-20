  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"