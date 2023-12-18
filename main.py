  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import random
def roll_die():
        return random.randint(1, 6)