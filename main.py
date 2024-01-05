  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
n = 10
print("Cube numbers:", [x**3 for x in range(n)])