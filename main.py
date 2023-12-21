  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list