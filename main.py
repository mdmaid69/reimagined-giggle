import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)