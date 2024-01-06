import random
def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)