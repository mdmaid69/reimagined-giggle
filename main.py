  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)