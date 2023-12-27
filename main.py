def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))