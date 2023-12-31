  import os
  def get_base_name(path):
        return os.path.basename(path)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)