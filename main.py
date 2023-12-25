import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value