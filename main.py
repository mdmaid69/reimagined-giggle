def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value