  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))