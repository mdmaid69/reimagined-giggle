  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import random
def roll_die():
        return random.randint(1, 6)