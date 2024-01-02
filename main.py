  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))