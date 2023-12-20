  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import random
def generate_random_choice(choices):
        return random.choice(choices)