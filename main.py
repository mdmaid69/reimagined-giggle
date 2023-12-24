import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])