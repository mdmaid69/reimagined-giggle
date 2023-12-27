import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)