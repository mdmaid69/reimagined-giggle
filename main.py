import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)