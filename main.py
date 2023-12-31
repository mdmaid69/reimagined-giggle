import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])