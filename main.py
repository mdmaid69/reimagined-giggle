import math
def calculate_permutations(n, k):
        return math.perm(n, k)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)