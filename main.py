import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))