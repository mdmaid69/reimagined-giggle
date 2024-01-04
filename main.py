  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b