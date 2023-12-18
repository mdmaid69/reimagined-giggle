import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))