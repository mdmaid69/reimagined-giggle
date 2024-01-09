import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)