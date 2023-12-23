  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))