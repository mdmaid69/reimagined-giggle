import random
def generate_random_choice(choices):
        return random.choice(choices)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)