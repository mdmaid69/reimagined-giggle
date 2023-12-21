  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import random
def roll_die():
        return random.randint(1, 6)