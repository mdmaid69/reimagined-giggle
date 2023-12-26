  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import random
def generate_random_choice(choices):
        return random.choice(choices)