import random
def roll_die():
        return random.randint(1, 6)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]