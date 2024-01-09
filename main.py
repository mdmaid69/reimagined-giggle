  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)