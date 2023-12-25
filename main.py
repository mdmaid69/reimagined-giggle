import random
def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def delete_file(file_name):
        os.remove(file_name)