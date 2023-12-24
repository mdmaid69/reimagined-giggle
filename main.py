import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))