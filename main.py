import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import itertools
print(list(itertools.permutations([1, 2, 3])))