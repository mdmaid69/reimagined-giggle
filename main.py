  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list