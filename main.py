import random
def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)