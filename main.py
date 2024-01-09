import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
from collections import Counter
print(Counter("hello world"))