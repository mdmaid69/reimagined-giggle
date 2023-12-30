  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array