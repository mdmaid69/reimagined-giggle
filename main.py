  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import math
def calculate_sign(x):
        return math.copysign(1, x)