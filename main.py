def is_even(n):
        return n % 2 == 0
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)