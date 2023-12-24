n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)