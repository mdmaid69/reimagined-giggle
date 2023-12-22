import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def get_list_from_array(array):
        return array.tolist()