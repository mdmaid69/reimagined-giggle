  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))