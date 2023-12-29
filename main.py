def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value