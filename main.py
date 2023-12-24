n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)