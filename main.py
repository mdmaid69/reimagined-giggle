  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))