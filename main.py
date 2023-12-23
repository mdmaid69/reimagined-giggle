import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def get_directory_name(path):
        return os.path.dirname(path)