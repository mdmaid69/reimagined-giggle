  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"