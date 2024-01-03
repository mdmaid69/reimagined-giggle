  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"