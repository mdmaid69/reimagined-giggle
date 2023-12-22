  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  def is_odd(n):
        return n % 2 != 0