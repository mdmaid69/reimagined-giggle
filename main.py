  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)