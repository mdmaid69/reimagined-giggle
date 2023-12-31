  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b