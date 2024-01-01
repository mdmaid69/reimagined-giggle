  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])