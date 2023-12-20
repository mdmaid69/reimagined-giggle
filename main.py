import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))