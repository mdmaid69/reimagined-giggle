  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)