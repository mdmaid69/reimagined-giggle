  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))