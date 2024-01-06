import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)