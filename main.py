  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b