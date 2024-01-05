  import os
  def get_base_name(path):
        return os.path.basename(path)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))