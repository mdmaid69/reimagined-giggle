  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import math
def calculate_logarithm_base_10(x):
        return math.log10(x)