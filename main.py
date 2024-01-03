  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import random
def generate_random_number(start, end):
        return random.randint(start, end)