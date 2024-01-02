  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])