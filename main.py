  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)