import math
def calculate_sign(x):
        return math.copysign(1, x)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"