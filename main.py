  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3