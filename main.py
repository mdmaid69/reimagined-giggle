import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"