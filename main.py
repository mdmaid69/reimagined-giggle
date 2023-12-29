  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)