  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import random
def roll_die():
        return random.randint(1, 6)