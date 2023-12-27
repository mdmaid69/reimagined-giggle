  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))