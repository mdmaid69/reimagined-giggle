import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])