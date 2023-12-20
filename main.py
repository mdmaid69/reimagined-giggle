import array
def convert_array_to_bytes(array):
        return array.tobytes()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))