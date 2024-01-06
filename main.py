import random
def roll_die():
        return random.randint(1, 6)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink