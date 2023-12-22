import array
def get_array_as_complex(array):
        return complex(array[0])
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))