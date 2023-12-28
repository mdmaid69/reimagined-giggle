  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)