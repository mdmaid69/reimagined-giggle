  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)