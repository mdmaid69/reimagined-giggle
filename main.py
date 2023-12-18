import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))