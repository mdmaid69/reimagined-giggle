import array
def get_array_length(array):
        return len(array)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))