  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
n = 10
print("Powers of 2:", [2**x for x in range(n)])