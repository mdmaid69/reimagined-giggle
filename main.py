  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)