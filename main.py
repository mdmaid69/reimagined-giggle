  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"