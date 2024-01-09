  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list