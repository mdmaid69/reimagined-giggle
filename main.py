n = 10
print("Powers of 2:", [2**x for x in range(n)])
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)