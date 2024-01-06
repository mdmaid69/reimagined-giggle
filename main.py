  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import random
def roll_die():
        return random.randint(1, 6)