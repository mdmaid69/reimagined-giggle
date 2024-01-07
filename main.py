  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])