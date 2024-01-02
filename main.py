  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)