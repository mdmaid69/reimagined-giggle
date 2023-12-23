import random
def generate_random_choice(choices):
        return random.choice(choices)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)