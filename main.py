  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))