  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))