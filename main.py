def calculate_average(lst):
        return sum(lst) / len(lst)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))