import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)