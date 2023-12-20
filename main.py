import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))