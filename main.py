  def is_even(n):
        return n % 2 == 0
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)