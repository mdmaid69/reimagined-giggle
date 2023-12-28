n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)