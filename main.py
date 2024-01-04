import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value