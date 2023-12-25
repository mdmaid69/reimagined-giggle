  def cube_number(x):
        return x**3
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))