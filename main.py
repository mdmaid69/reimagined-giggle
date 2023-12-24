  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)