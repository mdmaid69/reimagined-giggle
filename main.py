  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import array
def check_if_array_contains_item(array, item):
        return item in array