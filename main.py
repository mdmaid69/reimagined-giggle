import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"