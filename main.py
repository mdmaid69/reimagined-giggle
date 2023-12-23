  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import random
def roll_die():
        return random.randint(1, 6)