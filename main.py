  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import random
def generate_random_number(start, end):
        return random.randint(start, end)