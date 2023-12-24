n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value