  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))