  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)