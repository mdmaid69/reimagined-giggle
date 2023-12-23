  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)