import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"