  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import random
def generate_random_choice(choices):
        return random.choice(choices)