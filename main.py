  import math
  def calculate_square_root(n):
        return math.sqrt(n)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)