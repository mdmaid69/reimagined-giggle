def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)