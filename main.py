  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])