import itertools
print(list(itertools.permutations([1, 2, 3])))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)