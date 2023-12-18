numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)