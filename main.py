  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array