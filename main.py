import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)