def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)