n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value