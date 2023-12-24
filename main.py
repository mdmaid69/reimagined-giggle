  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list