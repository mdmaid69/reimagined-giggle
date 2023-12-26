  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)