def calculate_area_rectangle(l, w):
        return l * w
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))