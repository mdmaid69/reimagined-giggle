  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list