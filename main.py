  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)