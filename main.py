  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import random
def roll_die():
        return random.randint(1, 6)