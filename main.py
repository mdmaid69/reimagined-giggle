n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)