  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  def is_even(n):
        return n % 2 == 0