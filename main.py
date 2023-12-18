import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  import os
  def delete_file(file_name):
        os.remove(file_name)