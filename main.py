import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))