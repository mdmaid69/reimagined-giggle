  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)