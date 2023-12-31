  import os
  def delete_file(file_name):
        os.remove(file_name)
import random
def generate_random_choice(choices):
        return random.choice(choices)