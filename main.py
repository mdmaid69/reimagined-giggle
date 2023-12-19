  def multiply_numbers(x, y):
        return x * y
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))