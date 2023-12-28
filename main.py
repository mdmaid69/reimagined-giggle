  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import random
def roll_die():
        return random.randint(1, 6)