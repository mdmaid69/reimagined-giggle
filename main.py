import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)