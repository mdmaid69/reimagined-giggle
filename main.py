def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)