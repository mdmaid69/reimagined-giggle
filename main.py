  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import random
def roll_die():
        return random.randint(1, 6)