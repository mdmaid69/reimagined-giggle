import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))