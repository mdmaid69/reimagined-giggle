def calculate_area(radius):
        return 3.14 * radius * radius
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))