  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)