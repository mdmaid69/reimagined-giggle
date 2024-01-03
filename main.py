import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid