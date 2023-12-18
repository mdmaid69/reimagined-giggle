import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)