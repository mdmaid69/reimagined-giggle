n = 10
print("Square numbers:", [x**2 for x in range(n)])
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)