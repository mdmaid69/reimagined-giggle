import array
def get_array_buffer_info(array):
        return array.buffer_info()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))