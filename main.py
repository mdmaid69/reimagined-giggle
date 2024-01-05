  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list