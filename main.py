  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)