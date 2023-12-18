  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value