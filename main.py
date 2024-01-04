  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])