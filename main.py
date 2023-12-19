import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)