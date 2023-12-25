import random
def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def get_base_name(path):
        return os.path.basename(path)