import random
def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)