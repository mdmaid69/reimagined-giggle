  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_gamma_function(x):
        return math.gamma(x)