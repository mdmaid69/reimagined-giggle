def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))