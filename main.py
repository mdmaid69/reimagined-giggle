  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}