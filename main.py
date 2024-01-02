def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))