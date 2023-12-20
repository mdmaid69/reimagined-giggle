import random
def roll_die():
        return random.randint(1, 6)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)