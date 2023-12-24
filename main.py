  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import random
def generate_random_number(start, end):
        return random.randint(start, end)