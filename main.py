import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value