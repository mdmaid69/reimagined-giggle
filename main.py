  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])