import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)