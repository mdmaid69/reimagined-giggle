import random
def roll_die():
        return random.randint(1, 6)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize