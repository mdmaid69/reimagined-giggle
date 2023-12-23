  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)