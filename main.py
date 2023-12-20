  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import random
def generate_random_choice(choices):
        return random.choice(choices)