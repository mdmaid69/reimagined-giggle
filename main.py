import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import itertools
print(list(itertools.permutations([1, 2, 3])))