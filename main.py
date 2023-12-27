  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import random
def generate_random_choice(choices):
        return random.choice(choices)