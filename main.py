  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import random
def roll_die():
        return random.randint(1, 6)