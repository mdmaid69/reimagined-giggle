import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)