  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))