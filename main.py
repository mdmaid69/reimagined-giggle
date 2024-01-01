  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import os
def get_file_size(filename):
        return os.path.getsize(filename)