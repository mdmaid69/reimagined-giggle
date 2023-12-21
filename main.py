  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))