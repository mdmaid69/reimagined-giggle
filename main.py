import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()