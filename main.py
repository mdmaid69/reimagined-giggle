def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)