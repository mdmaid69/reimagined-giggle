  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)