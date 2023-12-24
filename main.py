  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list