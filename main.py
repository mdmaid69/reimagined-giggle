import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
i = 0
while i < 5:
        print(i)
        i += 1