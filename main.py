  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))