  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))