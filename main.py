  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)