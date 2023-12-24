  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import random
def roll_die():
        return random.randint(1, 6)