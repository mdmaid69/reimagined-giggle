import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size