import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))