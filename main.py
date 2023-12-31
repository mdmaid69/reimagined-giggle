  import os
  def get_current_working_directory():
        return os.getcwd()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"