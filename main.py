  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))