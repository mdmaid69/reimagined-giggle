  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)