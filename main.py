n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import collections
def count_elements(iterable):
        return collections.Counter(iterable)