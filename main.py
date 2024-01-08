import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"