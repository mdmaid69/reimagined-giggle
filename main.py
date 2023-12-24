  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])