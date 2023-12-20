  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)