  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])