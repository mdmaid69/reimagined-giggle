  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size