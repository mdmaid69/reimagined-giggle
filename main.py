import array
def iterate_over_array(array):
        for item in array:
        print(item)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))