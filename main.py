  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import random
def generate_random_choice(choices):
        return random.choice(choices)