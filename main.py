  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import random
def generate_random_choice(choices):
        return random.choice(choices)