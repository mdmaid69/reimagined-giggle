  def calculate_perimeter_triangle(a, b, c):
        return a + b + c
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))