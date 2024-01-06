import array
def get_array_as_memoryview(array):
        return memoryview(array)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))