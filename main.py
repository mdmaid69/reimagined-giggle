  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import random
def generate_random_number(start, end):
        return random.randint(start, end)