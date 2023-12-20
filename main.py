import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)