import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"