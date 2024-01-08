import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)