import collections
def count_elements(iterable):
        return collections.Counter(iterable)
n = 10
print("Square numbers:", [x**2 for x in range(n)])