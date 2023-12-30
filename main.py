import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
i = 0
while i < 5:
        print(i)
        i += 1