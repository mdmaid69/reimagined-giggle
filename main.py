  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import random
def generate_random_number(start, end):
        return random.randint(start, end)