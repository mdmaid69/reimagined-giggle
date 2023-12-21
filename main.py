import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))