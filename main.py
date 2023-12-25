import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b