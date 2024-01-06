  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list