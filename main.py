import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)