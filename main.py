  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import random
def roll_die():
        return random.randint(1, 6)