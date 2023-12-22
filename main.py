  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list