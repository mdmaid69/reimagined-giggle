  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import random
def generate_random_choice(choices):
        return random.choice(choices)