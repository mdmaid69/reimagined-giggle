  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import random
def roll_die():
        return random.randint(1, 6)