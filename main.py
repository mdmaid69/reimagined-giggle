  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))