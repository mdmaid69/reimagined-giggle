  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import random
def generate_random_number(start, end):
        return random.randint(start, end)