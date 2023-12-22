  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))