import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size