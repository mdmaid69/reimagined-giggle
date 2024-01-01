  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list