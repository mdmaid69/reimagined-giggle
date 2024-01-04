  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list