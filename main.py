def calculate_roi(gain, cost):
        return (gain - cost) / cost
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))