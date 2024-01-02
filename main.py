def calculate_work(force, distance):
        return force * distance
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))