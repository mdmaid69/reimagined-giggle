def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)