import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)