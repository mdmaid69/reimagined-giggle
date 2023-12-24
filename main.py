  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)