  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns