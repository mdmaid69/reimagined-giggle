import random
def generate_random_choice(choices):
        return random.choice(choices)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize