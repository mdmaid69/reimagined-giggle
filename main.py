import itertools
print(list(itertools.permutations([1, 2, 3])))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)