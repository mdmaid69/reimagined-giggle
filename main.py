import array
def get_string_from_array(array):
        return array.tobytes()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))