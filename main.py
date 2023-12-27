  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"