import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)