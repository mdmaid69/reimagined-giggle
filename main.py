numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))