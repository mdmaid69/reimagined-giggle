  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))