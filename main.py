import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"