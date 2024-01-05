  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
n = 10
print("Square numbers:", [x**2 for x in range(n)])