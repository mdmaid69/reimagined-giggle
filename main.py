import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
n = 10
print("Square numbers:", [x**2 for x in range(n)])