import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)