import math
def calculate_combinations(n, k):
        return math.comb(n, k)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"