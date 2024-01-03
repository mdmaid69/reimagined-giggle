import random
def generate_random_choice(choices):
        return random.choice(choices)
  import os
  def get_base_name(path):
        return os.path.basename(path)