  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import os
def change_working_directory(path):
        os.chdir(path)