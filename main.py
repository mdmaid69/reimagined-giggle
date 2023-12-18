import itertools
print(list(itertools.permutations([1, 2, 3])))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)