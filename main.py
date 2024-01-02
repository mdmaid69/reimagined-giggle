  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)