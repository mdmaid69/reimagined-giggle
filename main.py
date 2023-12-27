  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))