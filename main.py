  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))