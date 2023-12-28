import random
def roll_die():
        return random.randint(1, 6)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)