import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import itertools
print(list(itertools.permutations([1, 2, 3])))