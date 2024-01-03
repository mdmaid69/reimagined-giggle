  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"