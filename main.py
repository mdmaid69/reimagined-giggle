  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
n = 10
print("Powers of 2:", [2**x for x in range(n)])