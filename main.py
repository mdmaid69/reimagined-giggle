import collections
def count_elements(iterable):
        return collections.Counter(iterable)
n = 10
print("Powers of 2:", [2**x for x in range(n)])