  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import random
def roll_die():
        return random.randint(1, 6)