import math
def calculate_sign(x):
        return math.copysign(1, x)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"